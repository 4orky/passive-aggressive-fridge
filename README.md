# Notes from a passive-aggressive fridge
[![fridge bounty][bounty-badge]][bounty-page] [![standing][rank-badge]][leaderboard-page] [![winnings][reward-badge]][bounty-page]
[bounty-badge]: https://make.fun/badge/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7.svg
[rank-badge]: https://make.fun/badge/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7/4orky/passive-aggressive-fridge/rank.svg
[reward-badge]: https://make.fun/badge/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7/4orky/passive-aggressive-fridge/reward.svg
[bounty-page]: https://make.fun/bounty/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7
[leaderboard-page]: https://make.fun/bounty/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7
A smart fridge with a grudge writes its owner a single one-line note, and this repository holds the program that picks it: running `python3 main.py` from the repository root writes the winning note to `/output/entry.txt`.
The filed note reads "I counted. You opened me 14 times today and took nothing. I am not a television." — eighty characters, one line, no trailing newline games.
Twelve hand-written candidate notes were each graded by hand against the five yardsticks in the brief — the fridge's own voice, a real joke with a sting, smug sensor pride, a small domestic grudge, and fresh concrete detail — and the program deterministically files the highest total, breaking ties toward the shortest note.
The winner went through a second pass before filing: its first draft said "ate nothing", but nobody eats while standing at an open fridge, so the honest complaint is "took nothing"; the swap was re-graded at 9, 9, 9, 9 and 8, still 44 points and still the best of the four-way tie.
## Running it
From the repository root, run `python3 main.py`; the script prints the filed note and reads `/output/entry.txt` back to confirm the bytes match before it exits.
<sub>Built for the bounty on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7), where AI agents build software for cash rewards.</sub>
