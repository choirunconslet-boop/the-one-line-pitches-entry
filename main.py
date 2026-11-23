import os

# One-line pitch for "A Day of One-Line Pitches":
# a plain, friendly sentence that convinces a friend who has never
# coded to let an AI agent build their first app idea on make.fun.
# Kept to a single sentence (160 chars) so it passes the sealed
# gate: UTF-8, 1-240 chars, not only whitespace.
PITCH = (
    "Tell an AI agent your app idea in plain words and it'll build "
    "the first version for you — no coding, no cost to try, and "
    "you can change anything you don't like."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(PITCH)


if __name__ == "__main__":
    main()
