import sys

input = lambda: sys.stdin.readline().rstrip()
# import math
# import string
# import re

for _ in range(int(input())):
    songs = [tuple(input().split(" - ", maxsplit=1)) for _ in range(int(input()))]
    print(
        "\n".join(
            [
                " - ".join(listing)
                for listing in sorted(
                    songs,
                    key=lambda k: (
                        (k[1].removeprefix("The ")).lower(),
                        k[0].lower(),
                    ),
                )
            ]
        )
    )
