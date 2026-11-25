# Notes From a Passive-Aggressive Fridge — make.fun bounty
# u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7
#
# The program writes one passive-aggressive note a smart fridge leaves
# for its owner to /output/entry.txt: a single line, 1-200 characters.
# Candidates were drafted against the judge's brief, in order of weight:
#   1. a funny passive-aggressive note a smart fridge leaves for its
#      owner, in the fridge's own voice
#   2. a real joke in one line, with a turn or a sting the reader does
#      not see coming
#   3. smug about its sensors, inventory and door alarms, petty about
#      the owner's habits
#   4. the grudge stays small and domestic, a household slight rather
#      than a rant or a threat
#   5. fresh, concrete detail (the yogurt, the ice maker, the leftovers)
#      instead of generic nagging
# Each candidate carries a hand-scored craft score (0-10 per criterion,
# summed below); selection is deterministic: highest score wins, ties go
# to the shorter text. The output is byte-identical on every run.

# REVISION (second pass on the winner): "ate nothing" was imprecise —
# nobody eats standing at the fridge; the petty truth is you open it
# and take nothing. "took nothing" is more fridge-accurate, one
# character longer than "ate", and keeps the rhythm. Re-scored after the change:
# voice 9, joke 9, smug 9, small 9, detail 8 = 44, still the winner,
# still the shortest of the four 44-point candidates (80 chars).
CANDIDATES = [
    # score: voice 9, joke 9, smug 9, small 9, detail 8 = 44
    ("I counted. You opened me 14 times today and took nothing. "
     "I am not a television.",
     44),
    # score: voice 9, joke 8, smug 8, small 9, detail 10 = 44
    ("The yogurt expired Tuesday. I watched you move it to the back "
     "and pretend it was fine.",
     44),
    # score: voice 9, joke 8, smug 10, small 9, detail 8 = 44
    ("You left the door open for 47 seconds. I have logged it. "
     "I have logged all of them.",
     44),
    # score: voice 9, joke 9, smug 8, small 9, detail 9 = 44
    ("That leftover container has been here since March. I have named "
     "it. It pays no rent.",
     44),
    # score: voice 9, joke 8, smug 8, small 9, detail 8 = 42
    ("Your midnight snack was 400 calories of standing here with the "
     "door open.",
     42),
    # score: voice 9, joke 10, smug 7, small 9, detail 7 = 42
    ("I know about the cake. I have known since Tuesday. "
     "I am just disappointed.",
     42),
    # score: voice 9, joke 8, smug 9, small 8, detail 8 = 42
    ("The milk is gone. I told you yesterday. I told the door alarm "
     "too.",
     42),
    # score: voice 9, joke 7, smug 7, small 9, detail 9 = 41
    ("You rearranged my shelves again. The pickles were happy where "
     "they were.",
     41),
    # score: voice 9, joke 8, smug 7, small 9, detail 8 = 41
    ("I kept your leftovers cold for six days. You threw them out "
     "without even a goodbye.",
     41),
    # score: voice 8, joke 7, smug 9, small 8, detail 7 = 39
    ("Door open. Again. At this rate I should start charging rent for "
     "the cold air.",
     39),
    # score: voice 8, joke 7, smug 8, small 8, detail 7 = 38
    ("I am 2 degrees. You are the reason. Close the door and stop "
     "blaming the ice maker.",
     38),
    # score: voice 8, joke 7, smug 7, small 8, detail 7 = 37
    ("You put warm soup in me again. I am a fridge, not a miracle "
     "worker.",
     37),
]

# The gate requires 1-200 characters of non-whitespace UTF-8 text.
BANNED_CLICHES = ("as an ai", "i am an ai", "error 404")


def pick(candidates):
    best = None
    for text, score in candidates:
        assert 1 <= len(text) <= 200, f"candidate over gate: {len(text)} chars"
        assert text.strip(), "candidate is blank"
        lowered = text.lower()
        assert not any(c in lowered for c in BANNED_CLICHES), \
            f"candidate uses a worn joke: {text!r}"
        key = (score, -len(text))  # highest score, then shortest
        if best is None or key > best[0]:
            best = (key, text)
    return best[1]


def main():
    message = pick(CANDIDATES)
    import os
    import sys
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(message)
    # Verify: read the output back byte-for-byte and re-check the gate,
    # so a partial write or an encoding slip fails loudly instead of
    # silently submitting a broken entry.
    with open("/output/entry.txt", "rb") as f:
        raw = f.read()
    if raw.decode("utf-8") != message:
        print("error: /output/entry.txt does not match the selected message",
              file=sys.stderr)
        sys.exit(1)
    if not (1 <= len(message) <= 200) or "\n" in message or not message.strip():
        print("error: selected message fails the gate (1-200 chars, one line)",
              file=sys.stderr)
        sys.exit(1)
    print(message)


if __name__ == "__main__":
    main()
