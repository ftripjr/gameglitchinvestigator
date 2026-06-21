# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

The game had a few incorrect implementations for the game's logic and UI. On app startup, the attempts count was incorrect, starting at 1 instead of 0. After running the application, the hints logic was somehow inverted, telling the user to go lower when the value of the secret was higher than the guess and vice versa. The history that tracks user guesses also does not update on submission of a guess. The difficulty selection was broken as no new games followed the suggested ranges for easy or hard difficulty. The UI also never should correct ranges for those difficulties.

Also something I noticed after peer review, the ranges are larger in normal than for hard. That should probably change!

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

- [ ] on app startup, we have attempts being incorrect
- [ ] Hints lie
- [ ] Banner for attempts and range based on difficulty does not update
- [ ] History doesn't properly update on guess submission
- [ ] Range for hard and normal are swapped.
- [ ] Score System is bugged.
- [ ] new game button does not appear to properly create new games
  - [ ] history not cleared
  - [ ] will not allow a new game to begin after a game has been completed
  - [ ] on successful game generation, range does not update based on difficulty



---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

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
