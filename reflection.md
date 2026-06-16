# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|20 |"Go LOWER" | "Go HIGHER" |no history update, incorrect direction given to user |
|28 |"Go LOWER" | No change in UI, history delayed in update |previous history updated, current guess not added. |
|28 |"Go LOWER" | No change in UI, history delayed in update | |
|"New Game" pressed | history to clear|history not cleared | History not cleared|
|"New Game" pressed | Start a new game to play again banner should disappear. | Banner still visible. | inject.js:254 Uncaught TypeError: e.target.className.indexOf is not a function at HTMLDocument.mouseup (inject.js:254:67)|
|1->Pressed Enter key| WIN CASE | No change in tool | tool appears unresponsive. still has bad history |

So the bugs appear to be:

- [ ] Submitting a guess doesn't immediately update history
- [ ] Go Lower/Go Higher logic doesn't work
- [ ] New Game Button doesn't reset game history
- [ ] Attempts count starts at 1 instead of 0
- [ ] asdf

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? Claude
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

Gave Claude Code the following prompt:

`I tried resetting the game after guessing but pressing the button had no effect on the history or score.`

It told me, the following


> Found the bug! The "New Game" button (line 134) only resets attempts and secret, but doesn't clear history, score, or status. Let me fix it:

> Edit d:\ftripjr.dev\CodePath-Summer-2026\AI110\tinker_labs\game_glitch_investigator\gameglitchinvestigator\app.py
`

```python
if new_game:
  st.session_state.attempts = 0
  st.session_state.secret = random.randint(1, 100)
  # changes begin here
  st.session_state.history = []
  st.session_state.score = 0
  st.session_state.status = "playing"
  # changes end here
  st.success("New game started.")
  st.rerun()
```

I was able to fix the bug with the incorrect 

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
