# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable.

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

The Glitchy Guess Game is a guess the number game. It contains 3 difficulties and allows the player to see hints on whether their guess was too low or too high. The big problem is the game would lie to the player. There were bugs in score keeping, the range of numbers in the info element were hard coded in, the hints to the user would point to the opposite direction, and the score was not corrected as it should, along with a few other errors shown in [reflection.md](/reflection.md). I worked alongside Claude Coder (CC) to fix the bug by finding the inverted logic for hints, fixing the score updates, and getting rid of the hard-coded information in the info banner. I also used CC to learn more about state in Streamlit and how to save the needed attributes for the state of the guessing game and properly make new games with bounds based on the selected difficulty.

## 📸 Demo Walkthrough

```md
1. User enters a guess of 50
2. Game returns "Too High"
3. User enters a guess of 25 -> "Too High"
4. Score correctly deducts points after each wrong guess.
5. Game Ends after the correct guess or attempts run out.
6. User clicks "New Game" and tries again.
```

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```powershell

PS D:\ftripjr.dev\[...]\game-glitch-investigator> pytest .\tests\test_game_logic.py
==================================================================================================================================================================================== test session starts ====================================================================================================================================================================================
platform win32 -- Python 3.13.3, pytest-8.4.0, pluggy-1.6.0
rootdir: D:\ftripjr.dev\[...]\game-glitch-investigator
plugins: anyio-4.13.0
collected 21 items                                                                                                                                                                                                                                                                                                                                                                           

tests\test_game_logic.py .....................                                                                                                                                                                                                                                                                                                                                         [100%]

================================================================================================================================================== 21 passed in 0.02s ==================================================================================================================================================
PS D:\ftripjr.dev\[...]\game-glitch-investigator> 
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
