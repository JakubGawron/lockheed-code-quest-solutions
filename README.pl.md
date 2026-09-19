<h1 align="center">Lockheed Martin Code Quest - rozwiązania zadań konkursowych</h1>

<p align="center">
  <img src="./images/participant-badge-2025.png" alt="Code Quest 2025 Participant" width="49%">
  <img src="./images/participant-badge-2026.png" alt="Code Quest 2026 Participant" width="49%">
</p>

<p align="center">
  <a href="./README.md">English documentation</a>
</p>

<p align="center">
  Repozytorium zawiera uporządkowany zbiór moich rozwiązań zadań z poprzednich edycji konkursu
  <strong>Lockheed Martin Code Quest</strong>, pochodzących z platformy
  <a href="https://lmcodequestacademy.com/">Code Quest Academy</a>.
  Wszystkie zamieszczone rozwiązania zostały przesłane na stronę Code Quest Academy i <strong>potwierdzone jako poprawne</strong>
</p>

<p align="center">
  <img alt="Participant" src="https://img.shields.io/badge/Code%20Quest-2025%20Participant-purple">
  <img alt="Participant" src="https://img.shields.io/badge/Code%20Quest-2026%20Participant-purple">
  <br>
  <img alt="Python version" src="https://img.shields.io/badge/python-%3E%3D3.14-blue?logo=python&logoColor=white">
  <img alt="Built with uv" src="https://img.shields.io/badge/built%20with-uv-DE5FE9?logo=uv&logoColor=white">
  <img alt="Code style: Ruff" src="https://img.shields.io/badge/code%20style-ruff-black?logo=ruff&logoColor=white">
  <img alt="Version" src="https://img.shields.io/badge/version-1.0.0-informational">
  <img alt="Platform" src="https://img.shields.io/badge/platform-cross--platform-lightgrey">
  <img alt="Status" src="https://img.shields.io/badge/Status-Learning%20project-yellow">
  <img alt="License" src="https://img.shields.io/badge/license-MIT-lightgrey">
  <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/JakubGawron/lockheed-code-quest-solutions">
  <img alt="GitHub issues" src="https://img.shields.io/github/issues/JakubGawron/lockheed-code-quest-solutions">
  <img alt="Repo size" src="https://img.shields.io/github/repo-size/JakubGawron/lockheed-code-quest-solutions">
</p>

---

> **Uwaga:** To repozytorium powstało w **celach edukacyjnych** - żeby przed kolejnymi edycjami konkursu Lockheed Martin Code Quest podszlifować umiejętności związane z algorytmami, strukturami danych i programowaniem konkursowym. Code Quest to konkurs **drużynowy** - wziąłem w nim udział dwukrotnie: w **2025** roku (**4. miejsce**) oraz w **2026** roku (**8. miejsce**). To nieoficjalne repozytorium, niezwiązane bezpośrednio z Lockheed Martin.

---

## 📊 Postępy (stan na 16 września 2026)

| Poziom    | Status |     Postęp     |  Ukończono |    Rozwiązane |
| :-------- | :----: | :------------: | ---------: | ------------: |
| Practice  |   ✅   |   ▰▰▰▰▰▰▰▰▰▰   |    100.00% |         2 / 2 |
| Easy      |   🟡   |   ▰▰▰▰▰▰▰▰▰▱   |     89.29% |     100 / 112 |
| Medium    |   🟡   |   ▰▰▰▰▰▰▰▰▰▱   |     91.96% |     103 / 112 |
| Hard      |   🟡   |   ▰▱▱▱▱▱▱▱▱▱   |     13.58% |       11 / 81 |
| &nbsp;    | &nbsp; |     &nbsp;     |     &nbsp; |        &nbsp; |
| **Razem** | **📊** | **▰▰▰▰▰▰▰▱▱▱** | **70.36%** | **216 / 307** |

---

## 🧪 Testowanie rozwiązań

Każde rozwiązanie w tym repozytorium jest weryfikowane za pomocą zapisanych przypadków testowych (wejście/wyjście). Testy można uruchomić przy użyciu `uv` (zalecane) albo standardowego `pip`.

### Sposób 1: Za pomocą `uv` (zalecane)

`uv` to szybki, nowoczesny menedżer pakietów dla Pythona, który automatycznie zarządza zależnościami i środowiskami wirtualnymi.

**Instalacja `uv` (jeśli jeszcze go nie masz)**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Klonowanie repozytorium**

```bash
git clone https://github.com/JakubGawron/lockheed-code-quest-solutions
cd lockheed-code-quest-solutions
```

**Instalacja zależności**

```bash
uv sync
```

To polecenie instaluje dokładnie te wersje zależności, które są przypięte w pliku [`uv.lock`](./uv.lock), dzięki czemu środowisko jest w pełni odtwarzalne.

**Uruchamianie testów:**

```bash
uv run pytest -v                 # uruchamia wszystkie testy
uv run pytest -v -k addiply      # uruchamia tylko jedno zadanie (dopasowanie po nazwie folderu)
uv run pytest -x                 # zatrzymuje się na pierwszym niepowodzeniu
uv run pytest --tb=short         # skrócony widok błędów
uv run pytest -n auto            # uruchamia testy równolegle, na wszystkich dostępnych rdzeniach
uv run pytest -n 4               # uruchamia testy równolegle, na 4 rdzeniach
```

### Sposób 2: Za pomocą standardowego Pythona

**Klonowanie repozytorium**

```bash
git clone https://github.com/JakubGawron/lockheed-code-quest-solutions
cd lockheed-code-quest-solutions
```

**Tworzenie środowiska wirtualnego**

```bash
python -m venv .venv
source venv/bin/activate  # w Windows: venv\Scripts\activate
```

**Instalacja zależności**

```bash
python -m pip install "pytest>=9.1.1" "pytest-xdist>=3.8.0"
```

**Uruchamianie testów** (te same polecenia co wyżej, po aktywacji środowiska wirtualnego - wystarczy pominąć przedrostek `uv run`):

```bash
pytest -v                 # uruchamia wszystkie testy
pytest -v -k addiply      # uruchamia tylko jedno zadanie (dopasowanie po nazwie folderu)
pytest -x                 # zatrzymuje się na pierwszym niepowodzeniu
pytest --tb=short         # skrócony widok błędów
pytest -n auto            # uruchamia testy równolegle, na wszystkich dostępnych rdzeniach
pytest -n 4               # uruchamia testy równolegle, na 4 rdzeniach
```

---

## Uruchamianie wybranych testów za pomocą `-k`

Rozwiązania są podzielone według poziomu trudności na foldery (`practice/`, `easy/`, `medium/`, `hard/`), a w każdym z nich znajduje się osobny podfolder dla każdego zadania. Flaga `-k` w pytest dopasowuje słowa kluczowe do nazw testów i identyfikatorów węzłów, dzięki czemu można filtrować testy po poziomie trudności, po nazwie zadania albo po obu naraz:

```bash
uv run pytest -v -k "easy"                      # uruchamia wszystkie zadania z poziomu "easy"
uv run pytest -v -k "hard"                      # uruchamia wszystkie zadania z poziomu "hard"
uv run pytest -v -k "addiply"                   # uruchamia tylko zadanie "addiply", niezależnie od poziomu
uv run pytest -v -k "hard and addiply"          # uruchamia konkretnie "addiply" z poziomu hard
uv run pytest -v -k "easy or medium"            # uruchamia wszystko z poziomu easy LUB medium
uv run pytest -v -k "hard and not addiply"      # uruchamia wszystkie zadania z poziomu hard oprócz addiply"
```

---

## Licencja

Projekt jest udostępniany na licencji [MIT License](https://choosealicense.com/licenses/mit/).

Szczegóły znajdziesz w pliku [`LICENSE`](./LICENSE).

---

## Autor / Kontakt

- **Autor:** Jakub Gawron
- **GitHub:** [github.com/JakubGawron](https://github.com/JakubGawron)
- **Repozytorium:** [github.com/JakubGawron/lockheed-code-quest-solutions](https://github.com/JakubGawron/lockheed-code-quest-solutions)
- **Kontakt:** [contact.jakub.gawron@gmail.com](mailto:contact.jakub.gawron@gmail.com)
