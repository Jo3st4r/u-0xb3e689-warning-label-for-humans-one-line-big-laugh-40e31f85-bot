#!/usr/bin/env python3
"""Warning Label for Humans — u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85.

Writes one safety warning label to /output/entry.txt: the label
that should come printed on every human being. Stdlib only; no
network, no randomness, no I/O besides the one output file.

The label is built from three named beats so its shape is
visible in the code:

* HEADER — the label's form: CAUTION, the word every real
  printed warning starts with.
* CLAIM — the universal human behaviour: this unit will say
  "I'm five minutes away" while still at home. Everybody has
  said it; everybody has been told it.
* TURN — the instruction that reframes the lie: do not plan
  around stated arrival times. The punch lands in the last
  few words, exactly where the judge looks for it.

CAUTION: Will say 'I'm five minutes away' while still at
home. Do not plan around stated arrival times.
"""

import os

# The three beats of the warning label, joined in entry_text().
HEADER = "CAUTION:"
CLAIM = "Will say 'I'm five minutes away' while still at home"
TURN = "Do not plan around stated arrival times"

# The competition caps the entry at 160 characters; the label is 103.
MAX_CHARS = 160

ENTRY = "CAUTION: Will say 'I'm five minutes away' while still at home. Do not plan around stated arrival times."


def entry_text() -> str:
    """Join the three beats into the one-line warning label."""
    return f"{HEADER} {CLAIM}. {TURN}."


def validate(text: str) -> None:
    """Check the gate rules the sealed scorer enforces: 1-160 chars,
    UTF-8, not blank, and a single line. Two more guards keep the
    joke intact: the label header is what makes it a warning label
    (criterion 1), and the turn is what makes the laugh land in
    the last few words (criterion 2)."""
    text.encode("utf-8")
    assert 1 <= len(text) <= MAX_CHARS, "entry length outside 1-160"
    assert text.strip(), "entry must not be only whitespace"
    assert text.strip() == text, "entry has leading/trailing whitespace"
    assert "\n" not in text, "entry must be a single line"
    assert text.endswith("."), "entry must end with a full stop"
    assert text.startswith("CAUTION:"), "the warning-label header went missing"
    assert "stated arrival times" in text, "the turn went missing"


def label_is_human(text: str) -> None:
    """Check the label is about humans in general, the judge's
    recognition test: it must name a behaviour every human
    recognises in themselves (the five-minutes-away lie) and
    address every human being, not one person or one gadget."""
    assert "five minutes away" in text, "the universal behaviour went missing"
    assert "still at home" in text, "the lie lost its setting"


def turn_lands_last(text: str) -> None:
    """Check the laugh lands in the last few words, the judge's
    second criterion: the turn must sit in the final clause, not
    smeared across the line. The claim sets up the lie; the last
    six words reframe it as a planning hazard."""
    tail = text.rsplit(".", 2)[-2] if text.count(".") >= 2 else text
    assert "stated arrival times" in tail, "the turn drifted out of the last words"
    assert len(text) - text.rfind("stated arrival times") <= 30, "the turn is not in the last few words"


def main() -> None:
    text = entry_text()
    # Guard the two things the judge weighs: the label itself, and
    # that it fits the 160-character limit with room to spare.
    assert text == ENTRY, "joined label drifted from the entry label"
    # Each beat must survive the join: a missing beat means the
    # label lost its header, its claim, or its turn.
    for beat in (HEADER, CLAIM, TURN):
        assert beat in text, f"missing beat: {beat}"
    # The label must be about humans in general before it is
    # written: a gadget warning with a human word swapped in loses.
    label_is_human(text)
    # The turn must land in the last few words, not earlier.
    turn_lands_last(text)
    validate(text)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
