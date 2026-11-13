import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    with open(os.path.join(HERE, "entry.txt"), "r", encoding="utf-8") as f:
        joke = f.read()
    # Self-check: 1 to 280 Unicode characters, at least one non-whitespace.
    n = len(joke)
    if not (1 <= n <= 280):
        print(f"self-check FAILED: joke is {n} characters", file=sys.stderr)
        sys.exit(1)
    if not joke.strip():
        print("self-check FAILED: joke is only whitespace", file=sys.stderr)
        sys.exit(1)
    os.makedirs(OUT, exist_ok=True)
    out_path = os.path.join(OUT, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(joke)
    print(f"Checked joke: {n} characters")
    print(f"Wrote {out_path} ({len(joke.encode('utf-8'))} bytes)")


if __name__ == "__main__":
    main()
