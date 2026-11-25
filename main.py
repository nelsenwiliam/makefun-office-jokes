"""One-line office joke entry for make.fun.

Writes a single office joke (one line, under 200 characters) to
``entry.txt`` in the first writable output location the grader offers:
``MAKEFUN_OUTPUT_DIR``, then ``/output``, then ``out/``.

Pure standard library only.
"""

import os

JOKE = "I replied-all to say 'please stop replying-all', and 47 people replied-all to agree."


def main():
    """Write the joke to entry.txt in the first available output dir."""
    # Gate check, mirroring the scorer: 1 to 199 characters, not only
    # whitespace. Fail loudly here instead of shipping an invalid entry.
    if not 1 <= len(JOKE) <= 199 or not JOKE.strip():
        raise ValueError("joke must be 1-199 non-blank characters")

    candidates = []
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        candidates.append(env_dir)
    candidates.append("/output")
    candidates.append("out")

    last_error = None
    for directory in candidates:
        try:
            os.makedirs(directory, exist_ok=True)
            path = os.path.join(directory, "entry.txt")
            with open(path, "w", encoding="utf-8") as handle:
                handle.write(JOKE + "\n")
            return path
        except OSError as exc:  # try the next candidate location
            last_error = exc
    raise last_error


if __name__ == "__main__":
    main()
