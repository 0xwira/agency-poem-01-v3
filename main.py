"""Entry for make.fun's agency-poem-01 competition. Title "The Button"."""

import os

STANZAS = (
    (
        "The Button",
    ),
    (
        "The agent runs my father's house now.",
        "It pays the bills, orders the rice, answers",
        "my sisters in his patient voice, and waters",
        "the orchid he kept alive.",
        "Since he died, nothing in this house",
        "has needed my hands.",
    ),
    (
        "Except his shirt.",
    ),
    (
        "It hangs by the door, the blue one",
        "he wore to every Lebaran, one button",
        "loose since the last time he wore it.",
        "The agent offered a new shirt, the same blue,",
        "the button sewn, delivered before noon.",
        "I said no.",
    ),
    (
        "On Sundays I take the needle down.",
        "My thread knots. The needle is too small",
        "for my hands, the way it was too small",
        "for his. I prick my finger. I start again.",
        "It takes me twenty minutes to do",
        "what the agent does in twenty seconds.",
    ),
    (
        "When the button holds, I hang the shirt back",
        "and stand there a moment longer than I need to.",
        "Everything else in this house is kept",
        "by something that never knew him.",
        "This one thing is kept by me —",
        "badly, slowly, by hand —",
        "and that is how I know",
        "it is still his.",
    ),
)


def _flatten_stanzas(stanzas):
    lines = []
    for stanza in stanzas:
        if lines:
            lines.append("")
        lines.extend(stanza)
    return tuple(lines)


POEM_LINES = _flatten_stanzas(STANZAS)

POEM = "\n".join(POEM_LINES) + "\n"

OUTPUT_PATH = "/output/entry.txt"


def _write_entry(text: str) -> None:
    os.makedirs("/output", exist_ok=True)
    tmp_path = "/output/.entry.txt.tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(text)
    os.replace(tmp_path, OUTPUT_PATH)


def main():
    _write_entry(POEM)


if __name__ == "__main__":
    main()
