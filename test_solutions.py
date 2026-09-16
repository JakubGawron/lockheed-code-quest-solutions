"""Generic test runner for competitive-programming style solutions.

Layout expected::

    mainproject/
        test_solutions.py          <- this file
        easy/
            addiply/
                addiply.py         <- solution, named after its folder
                1.in               <- input
                1.ans              <- expected output
                2.in
                2.ans
        medium/
        hard/
        practice/

Each test case's ID is ``<category>-<problem>-<case>``, e.g.
``easy-addiply-1``. That naming is what makes the ``-k`` filters below work.

A problem folder with a solution that is still a stub (empty file, or a body
that's just ``pass`` / ``...`` / ``raise NotImplementedError``) is reported
as *skipped*, not failed — write your solution and it starts running for
real. A problem folder with no ``1.in`` / ``1.ans`` pair, or no solution file
at all, is reported as a *failing* test instead, since that's a setup
mistake worth noticing rather than a "not implemented yet" placeholder.

Usage::

    # Run everything
    uv run pytest -v

    # Run one problem, any category (matches the problem's folder name)
    uv run pytest -v -k addiply

    # Run one category, every problem in it
    uv run pytest -v -k easy
    uv run pytest -v -k medium

    # Run one problem within one specific category
    uv run pytest -v -k "easy and addiply"

    # Run a single test case of a single problem
    uv run pytest -v -k "easy-addiply-1"

    # Run everything except one category / one problem
    uv run pytest -v -k "not hard"
    uv run pytest -v -k "not addiply"

    # Stop at the first failure
    uv run pytest -x

    # Shorter failure output
    uv run pytest --tb=short

    # Run in parallel (uv add --dev pytest-xdist)
    uv run pytest -n auto
"""

from __future__ import annotations

import os
import subprocess
import sys
from collections.abc import Iterator, Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import Final

import pytest

ROOT: Final[Path] = Path(__file__).parent

#: All category folders live under this directory, one level below ROOT.
SOLUTIONS_DIR: Final[Path] = ROOT / "solutions"

#: Categories are scanned in this order. Any other top-level directory is
#: ignored, so virtualenvs, caches and tooling folders never get collected.
CATEGORIES: Final[tuple[str, ...]] = ("easy", "medium", "hard", "practice")

#: Per-case wall-clock limit for the solution process, overridable with
#: ``CP_TIMEOUT=10 uv run pytest``.
TIMEOUT_SECONDS: Final[float] = float(os.environ.get("CP_TIMEOUT", "5"))

INPUT_SUFFIX: Final[str] = ".in"
EXPECTED_SUFFIX: Final[str] = ".ans"
ENCODING: Final[str] = "utf-8"

_IGNORED_PREFIXES: Final[tuple[str, ...]] = (".", "_")


# --------------------------------------------------------------------------- #
# Case model
# --------------------------------------------------------------------------- #


@dataclass(frozen=True, slots=True)
class RunCase:
    """A solution plus one input/expected-output pair to run it against."""

    category: str
    problem: str
    case_id: str
    solution: Path
    input_file: Path
    expected_file: Path

    @property
    def test_id(self) -> str:
        return f"{self.category}-{self.problem}-{self.case_id}"


@dataclass(frozen=True, slots=True)
class BrokenProblem:
    """A problem folder that cannot be run.

    Surfaced as a failing test by default. Set ``skip=True`` for cases that
    are expected/benign (e.g. an untouched placeholder solution) so they show
    up as *skipped* instead of *failed*.
    """

    category: str
    problem: str
    reason: str
    case_id: str = "collect"
    skip: bool = False

    @property
    def test_id(self) -> str:
        return f"{self.category}-{self.problem}-{self.case_id}"


type Case = RunCase | BrokenProblem


# --------------------------------------------------------------------------- #
# Discovery
# --------------------------------------------------------------------------- #


def _natural_key(name: str) -> tuple[int, int, str]:
    """Sort ``1, 2, 10`` numerically while keeping non-numeric names stable."""
    if name.isdigit():
        return (0, int(name), "")
    return (1, 0, name)


def _is_visible_dir(path: Path) -> bool:
    return path.is_dir() and not path.name.startswith(_IGNORED_PREFIXES)


def _iter_problem_dirs() -> Iterator[tuple[str, Path]]:
    """Yield ``(category, problem_dir)`` for every problem folder on disk."""
    for category in CATEGORIES:
        category_dir: Path = SOLUTIONS_DIR / category
        if not category_dir.is_dir():
            continue
        for problem_dir in sorted(category_dir.iterdir(), key=lambda p: p.name):
            if _is_visible_dir(problem_dir):
                yield category, problem_dir


#: Statements that, alone, mean "nothing implemented yet".
_PLACEHOLDER_BODIES: Final[frozenset[str]] = frozenset(
    {
        "pass",
        "...",
        "raise NotImplementedError",
    }
)


def _is_placeholder_solution(solution: Path) -> bool:
    """True if the file has no real logic yet (empty, comments only, or a
    single ``pass`` / ``...`` / ``raise NotImplementedError`` statement,
    optionally under an ``if __name__ == "__main__":`` guard)."""
    source = solution.read_text(encoding=ENCODING)

    code_lines: list[str] = []
    for raw_line in source.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith(('"""', "'''")):
            continue  # best-effort: skip docstring lines
        code_lines.append(line.rstrip(":"))

    if not code_lines:
        return True

    meaningful = [
        line
        for line in code_lines
        if line not in ('if __name__ == "__main__"', "if __name__ == '__main__'")
    ]
    if not meaningful:
        return True

    return all(
        line in _PLACEHOLDER_BODIES or line.startswith("raise NotImplementedError(")
        for line in meaningful
    )


def _find_solution(problem_dir: Path) -> Path | None:
    """Prefer ``<problem>/<problem>.py``; fall back to a lone ``*.py`` file."""
    preferred = problem_dir / f"{problem_dir.name}.py"
    if preferred.is_file():
        return preferred

    candidates = [
        path
        for path in sorted(problem_dir.glob("*.py"))
        if not path.name.startswith(_IGNORED_PREFIXES + ("test_",))
    ]
    return candidates[0] if len(candidates) == 1 else None


def discover_cases() -> list[Case]:
    """Build the full, deterministically ordered list of cases to run."""
    cases: list[Case] = []

    for category, problem_dir in _iter_problem_dirs():
        problem = problem_dir.name

        solution = _find_solution(problem_dir)
        if solution is None:
            cases.append(
                BrokenProblem(
                    category,
                    problem,
                    f"no solution found in {problem_dir} "
                    f"(expected {problem}.py, or exactly one *.py file)",
                )
            )
            continue

        if _is_placeholder_solution(solution):
            cases.append(
                BrokenProblem(
                    category,
                    problem,
                    f"{solution.name} is still a placeholder (not implemented yet)",
                    skip=True,
                )
            )
            continue

        inputs = sorted(
            problem_dir.glob(f"*{INPUT_SUFFIX}"),
            key=lambda path: _natural_key(path.stem),
        )
        if not inputs:
            cases.append(
                BrokenProblem(
                    category,
                    problem,
                    f"no test cases in {problem_dir} "
                    f"(expected at least 1{INPUT_SUFFIX} and 1{EXPECTED_SUFFIX})",
                )
            )
            continue

        for input_file in inputs:
            expected_file: Path = input_file.with_suffix(EXPECTED_SUFFIX)
            if not expected_file.is_file():
                cases.append(
                    BrokenProblem(
                        category,
                        problem,
                        f"missing {expected_file.name} for {input_file.name}",
                        case_id=input_file.stem,
                    )
                )
                continue

            cases.append(
                RunCase(
                    category=category,
                    problem=problem,
                    case_id=input_file.stem,
                    solution=solution,
                    input_file=input_file,
                    expected_file=expected_file,
                )
            )

    if not cases:
        cases.append(
            BrokenProblem(
                "solutions",
                "problems",
                f"no problems discovered under {SOLUTIONS_DIR} "
                f"(expected category folders: {', '.join(CATEGORIES)})",
            )
        )

    return cases


CASES: Final[Sequence[Case]] = tuple(discover_cases())
CASE_IDS: Final[Sequence[str]] = tuple(case.test_id for case in CASES)


# --------------------------------------------------------------------------- #
# Execution
# --------------------------------------------------------------------------- #


def normalize(text: str) -> str:
    """Ignore trailing whitespace/newline differences that shouldn't fail a test."""
    return "\n".join(line.rstrip() for line in text.strip().splitlines())


def _run_solution(case: RunCase, stdin_data: str) -> subprocess.CompletedProcess[str]:
    try:
        return subprocess.run(
            [sys.executable, str(case.solution)],
            input=stdin_data,
            capture_output=True,
            text=True,
            encoding=ENCODING,
            timeout=TIMEOUT_SECONDS,
            cwd=case.solution.parent,
            check=False,
        )
    except subprocess.TimeoutExpired:
        pytest.fail(
            f"{case.test_id}: timed out after {TIMEOUT_SECONDS:g}s",
            pytrace=False,
        )


@pytest.mark.parametrize("case", CASES, ids=CASE_IDS)
def test_solution(case: Case) -> None:
    if isinstance(case, BrokenProblem):
        if case.skip:
            pytest.skip(case.reason)
        pytest.fail(case.reason, pytrace=False)

    stdin_data: str = case.input_file.read_text(encoding=ENCODING)
    expected: str = case.expected_file.read_text(encoding=ENCODING)

    result: subprocess.CompletedProcess[str] = _run_solution(case, stdin_data)

    assert result.returncode == 0, (
        f"{case.test_id} exited with {result.returncode}:\n{result.stderr}"
    )
    assert normalize(result.stdout) == normalize(expected), (
        f"\n--- input ({case.input_file.name}) ---\n{stdin_data}"
        f"\n--- expected ({case.expected_file.name}) ---\n{expected}"
        f"\n--- got ---\n{result.stdout}"
        + (f"\n--- stderr ---\n{result.stderr}" if result.stderr else "")
    )
