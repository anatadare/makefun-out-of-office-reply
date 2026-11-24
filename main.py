import os

SETUP = "Out of office: I took my context window on holiday with me, "
PUNCHLINE = "so I have forgotten who you are, what this is, and why I am replying."

REPLY = SETUP + PUNCHLINE

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 160


def main():
    text = REPLY.strip()
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(f"reply is {len(text)} chars, must be 1-{MAX_CHARS}")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
