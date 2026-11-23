"""Make the AI Judge Laugh: Office Jokes.

Writes one single-line joke about office life to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt when set).

Pure Python standard library only; no network access.
"""

import os

JOKE = (
    "Our office plants died, so facilities replaced them with a poster "
    "of plants and a meeting about morale \u2014 the poster is thriving."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    # Guard: a single line, 1-199 characters, nothing else.
    # Explicit checks (not assert) so they survive `python -O`.
    joke = JOKE.strip()
    if "\n" in joke or "\r" in joke:
        raise ValueError("joke must be a single line")
    if not 1 <= len(joke) <= 199:
        raise ValueError("joke must be 1-199 characters")

    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(joke)
    os.chmod(path, 0o644)

    # Read back and verify: what landed on disk must be exactly the joke.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != joke:
        raise ValueError("entry.txt does not match the joke")


if __name__ == "__main__":
    main()
