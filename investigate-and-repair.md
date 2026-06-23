# Phase 2: Investigate and Repair

## What bugs should I fix?

Required:

- [x] Hints lie to player
- [x] Attempts start at 1 on app start instead of 0
- [x] Info Banner does not update
  - [x] Info block has `1 to 100` is hard coded instead of showing the range based on difficulty selection.
- [x] new game button does not appear to properly create new games
  - [x] new game does not begin after a game has been completed
  - [x] history not cleared
  - [x] on successful game generation, range does not update based on difficulty

Stretch Goals:

- [x] History is not properly cleared on new game.
- [x] Ranges and Guesses are not consistent with difficulty
  - [x] "Easy" -> Smallest Range (1,20) and Most Guesses (8)
  - [x] "Normal" -> Medium Range (1,50) and Medium Guesses (6)
  - [x] "Hard" -> Largest Range (1,100) and Least Guesses (5)
- [ ] Guesses remaining are not consistent with submissions.
- [ ] History is not properly updated with user submissions.
- [ ] Score System is bugged.
