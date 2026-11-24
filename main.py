"""One-line office joke for the make.fun "One-Line Office Joke: 24-Hour Sprint" bounty.

Writes a single original line of office humor to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt), exactly the line's bytes, with no trailing newline.
"""

LINE = "The meeting that should have been an email just scheduled a follow-up meeting to discuss why it wasn't an email."

assert 1 <= len(LINE) <= 200 and LINE.strip(), "LINE must be 1-200 chars and not only whitespace"


def main() -> None:
    import os
    from pathlib import Path

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(LINE.encode("utf-8"))


if __name__ == "__main__":
    main()
