# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

The game had a few incorrect implementations for the game's logic and UI. On app startup, the attempts count was incorrect, starting at 1 instead of 0. After running the application, the hints logic was somehow inverted, telling the user to go lower when the value of the secret was higher than the guess and vice versa. The history that tracks user guesses also does not update on submission of a guess. The difficulty selection was broken as no new games followed the suggested ranges for easy or hard difficulty. The UI also never should correct ranges for those difficulties.

Also something I noticed after peer review, the ranges are larger in normal than for hard and the guesses don't seem to be consistent based on difficulty. That should probably change!

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

Run #1 

|         Input          |  Expected Behavior  |    Actual Behavior    |               Console Output / Error                 |
|------------------------|---------------------|-----------------------|------------------------------------------------------|
|       (app start)      |      Attempts: 0    |      Attempts: 1      |                    no errors shown                   |
|           50           |      "Go LOWER"     |      "Go HIGHER!"     |                    no errors shown                   |
|           75           |      "Go LOWER"     |    No change in UI    |                    no errors shown                   |
|           75           |      "Go LOWER"     |      "Go HIGHER!"     |                    no errors shown                   |
|          100           |      "Go LOWER"     |    No change in UI    |                    no errors shown                   |
|          100           |      "Go LOWER"     |       "Go LOWER"      |                    no errors shown                   |
|           33           |    "You Won! ..."   |     "You Won! ..."    |                    no errors shown                   |
|   "Easy" Difficulty    |   Difficulty: Easy  | Winner alert changed. |inject.js:254 Uncaught TypeError: e.target.className.indexOf is not a function at HTMLDocument.mouseup (inject.js:254:67)|
|   "New Game" pressed   |     history clear   |   history unchanged   |                    no errors shown                   |
|   "New Game" pressed   |  Alert disappears.  | Banner still visible. |                    no errors shown                   |

Run #2

|         Input          |  Expected Behavior  |    Actual Behavior    |               Console Output / Error                 |
|------------------------|---------------------|-----------------------|------------------------------------------------------|
|           33           |     Score: 100      |       Score: 70       | no history update, incorrect direction given to user |
|   "Easy" Difficulty    |   Difficulty: Easy  | Winner alert changed. |inject.js:254 Uncaught TypeError: e.target.className.indexOf is not a function at HTMLDocument.mouseup (inject.js:254:67)|
|   "New Game" pressed   |     history clear   |   history unchanged   |                    no errors shown                   |
|   "New Game" pressed   |     history clear   |   history unchanged   |                    no errors shown                   |
|   "New Game" pressed   |  Alert disappears.  | Banner still visible. |                    no errors shown                   |

Run # 3

|         Input          |  Expected Behavior  |    Actual Behavior    |               Console Output / Error                 |
|------------------------|---------------------|-----------------------|------------------------------------------------------|
|           69           |      Score: 100     |       Score: 80       |                    no errors shown                   |
|   "Easy" Difficulty    |   Difficulty: Easy  | Winner alert changed. |inject.js:254 Uncaught TypeError: e.target.className.indexOf is not a function at HTMLDocument.mouseup (inject.js:254:67)|
|   "New Game" pressed   |      Score: 0     |       Score: 80       |                    no errors shown                   |
|   "New Game" pressed   |     history clear   |   history unchanged   |                    no errors shown                   |
|   "New Game" pressed   |  Alert disappears.  | Banner still visible. |                    no errors shown                   |ame.indexOf is not a function at HTMLDocument.mouseup (inject.js:254:67)|


So the bugs appear to be:

Required:

- [ ] Hints lie to player
- [ ] Attempts start at 1 on app start instead of 0
- [ ] Info Banner does not update
  - [ ] Info block has `1 to 100` is hard coded instead of showing the range based on difficulty selection.
- [ ] new game button does not appear to properly create new games
  - [ ] new game does not begin after a game has been completed
  - [ ] history not cleared
  - [ ] on successful game generation, range does not update based on difficulty
- [ ] History is not properly cleared on new game.
- [ ] Ranges and Guesses are not consistent with difficulty
  - [ ] "Easy" -> Smallest Range (1,20) and Most Guesses (8)
  - [ ] "Normal" -> Medium Range (1,50) and Medium Guesses (6)
  - [ ] "Hard" -> Largest Range (1,100) and Least Guesses (5)
- [ ] Guesses remaining are not consistent with submissions.
- [ ] History is not properly updated with user submissions.
- [ ] Score System is bugged.

---

## 2. How did you use AI as a teammate?

I used Claude Code to help me fix the following glitches:

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

Claude Code had a pretty easy time correcting almost all the "required" bugs. It easily dealt with recognizing when values that needed to be dynamic were hard-coded and findig off by one errors like with the attempts value on startup. But neither Claude Code nor I was able to figure out  how to correct the history submission bug that should have updated the history of the game on submission of a guess.

My conversations with Claude Code can be found in [`ai_interactions.md`](/ai_interactions.md)

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
