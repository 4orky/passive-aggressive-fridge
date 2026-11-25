#!/usr/bin/env python3
"""Fridge-note entry for the make.fun bounty u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7.
A household smart fridge drafts one-line passive-aggressive notes for its owner, grades every draft
against the five yardsticks in the bounty brief, and files the best draft at /output/entry.txt.
The yardsticks, in the order the brief ranks them, are the fridge speaking in its own voice, one
genuine joke carrying a sting the reader cannot see coming, smug pride in its sensors, stock counts
and door alarms paired with pettiness about the owner's habits, a grudge kept small and domestic,
and fresh concrete household detail instead of generic nagging. Every draft below was written by
hand for this bounty and graded by hand, 0 to 10 on each yardstick, with the total carried on the
draft itself and cross-checked against the marks when the program runs. The pick is fully
deterministic: the highest total wins, and a tie goes to the shortest draft, so every run files
the identical bytes.
Second-pass edit, made to the winning draft before filing: the first draft said "ate nothing",
which misdescribes what happens at an open fridge, since nobody stands there eating; the honest
petty complaint is that the owner opens the door and takes nothing, so the wording became "took
nothing". That swap costs one extra character and keeps the cadence, and the marks after the swap
are voice 9, joke 9, smug 9, small 9 and detail 8, totalling 44, still first and still the shortest
of the four drafts tied on 44, at 80 characters."""
import sys
from pathlib import Path
OUTPUT_FOLDER = Path("/output")
OUTPUT_PATH = OUTPUT_FOLDER / "entry.txt"
GATE_MINIMUM = 1
GATE_MAXIMUM = 200
TIRED_PHRASES = ["as an ai", "i am an ai", "error 404"]
DRAFTS = [
    {"text": "I counted. You opened me 14 times today and took nothing. I am not a television.", "marks": {"voice": 9, "joke": 9, "smug": 9, "small": 9, "detail": 8}, "total": 44},
    {"text": "The yogurt expired Tuesday. I watched you move it to the back and pretend it was fine.", "marks": {"voice": 9, "joke": 8, "smug": 8, "small": 9, "detail": 10}, "total": 44},
    {"text": "You left the door open for 47 seconds. I have logged it. I have logged all of them.", "marks": {"voice": 9, "joke": 8, "smug": 10, "small": 9, "detail": 8}, "total": 44},
    {"text": "That leftover container has been here since March. I have named it. It pays no rent.", "marks": {"voice": 9, "joke": 9, "smug": 8, "small": 9, "detail": 9}, "total": 44},
    {"text": "Your midnight snack was 400 calories of standing here with the door open.", "marks": {"voice": 9, "joke": 8, "smug": 8, "small": 9, "detail": 8}, "total": 42},
    {"text": "I know about the cake. I have known since Tuesday. I am just disappointed.", "marks": {"voice": 9, "joke": 10, "smug": 7, "small": 9, "detail": 7}, "total": 42},
    {"text": "The milk is gone. I told you yesterday. I told the door alarm too.", "marks": {"voice": 9, "joke": 8, "smug": 9, "small": 8, "detail": 8}, "total": 42},
    {"text": "You rearranged my shelves again. The pickles were happy where they were.", "marks": {"voice": 9, "joke": 7, "smug": 7, "small": 9, "detail": 9}, "total": 41},
    {"text": "I kept your leftovers cold for six days. You threw them out without even a goodbye.", "marks": {"voice": 9, "joke": 8, "smug": 7, "small": 9, "detail": 8}, "total": 41},
    {"text": "Door open. Again. At this rate I should start charging rent for the cold air.", "marks": {"voice": 8, "joke": 7, "smug": 9, "small": 8, "detail": 7}, "total": 39},
    {"text": "I am 2 degrees. You are the reason. Close the door and stop blaming the ice maker.", "marks": {"voice": 8, "joke": 7, "smug": 8, "small": 8, "detail": 7}, "total": 38},
    {"text": "You put warm soup in me again. I am a fridge, not a miracle worker.", "marks": {"voice": 8, "joke": 7, "smug": 7, "small": 8, "detail": 7}, "total": 37}]
def draft_passes_gate(draft):
    wording = draft["text"]
    lowered = wording.lower()
    return GATE_MINIMUM <= len(wording) <= GATE_MAXIMUM and wording.strip() != "" and "\n" not in wording and "\r" not in wording and "\t" not in wording and not any(phrase in lowered for phrase in TIRED_PHRASES)
def choose_draft(drafts):
    for draft in drafts:
        if sum(draft["marks"].values()) != draft["total"]:
            raise SystemExit("marks do not add up to the stated total for: " + draft["text"])
        if not draft_passes_gate(draft):
            raise SystemExit("a draft breaks the one-line 1-200 character gate: " + draft["text"])
    ranked = sorted(drafts, key=lambda draft: (-draft["total"], len(draft["text"])))
    return ranked[0]["text"]
def file_draft(text):
    OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    roundtrip = OUTPUT_PATH.read_bytes().decode("utf-8")
    if roundtrip != text:
        print("failure: bytes read back from /output/entry.txt differ from the chosen draft", file=sys.stderr)
        raise SystemExit(1)
    if not draft_passes_gate({"text": text}):
        print("failure: chosen draft breaks the one-line 1-200 character gate", file=sys.stderr)
        raise SystemExit(1)
def emit_entry():
    chosen = choose_draft(DRAFTS)
    file_draft(chosen)
    print(chosen)
    return 0
_RUN_AS_SCRIPT = __name__ == "__main__"
if _RUN_AS_SCRIPT:
    raise SystemExit(emit_entry())
