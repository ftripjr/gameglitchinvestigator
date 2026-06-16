# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

<!-- Describe the goal you asked the agent to accomplish -->

**What did the agent do?**

<!-- List the steps the agent took (files edited, commands run, etc.) -->

**What did you have to verify or fix manually?**

<!-- Describe anything the agent got wrong or that required human review -->

My first question to Claude was the following:

> I ran out of guesses doing a hard difficulty version of the game and was told to make a guess of a number between 1 and 100 even though the range for a hard game should be 1 and 50. Why would the banner that tells the user to "Guess a number between 1 and 100." incorrectly show the bounds of the game?

Claude responded with the following:

```
 The user is asking about a bug in a game where the banner showing the number range is incorrect. For a hard difficulty game, the range should be 1-50, but the banner is showing 1-100 instead.

Let me look at the app.py file to understand the game logic and see where this bug might be coming from.

The user has opened app.py in the IDE, so let me read that file to understand the code structure.

Let me examine the app.py file to see where the banner message is generated.

Read [...]\game-glitch-investigator\app.py
Found the bug! Looking at lines 109-112:

st.info(
    f"Guess a number between 1 and 100. "
    f"Attempts left: {attempt_limit - st.session_state.attempts}"
)
The banner at line 109-110 is hardcoded to say "Guess a number between 1 and 100" instead of using the actual range values that were computed on lines 87-88:


low, high = get_range_for_difficulty(difficulty)
So the banner should use the low and high variables instead of hardcoding "1 and 100".

This is why when playing Hard difficulty (which should be 1-50), the banner still shows "1 and 100".

Found the bug! On line 109-110, the banner message is hardcoded to "Guess a number between 1 and 100" instead of using the actual range for the difficulty level.


st.info(
    f"Guess a number between 1 and 100. "  # ← Hard-coded, ignores difficulty!
    f"Attempts left: {attempt_limit - st.session_state.attempts}"
)
The code already correctly computes the range on lines 87-88:


low, high = get_range_for_difficulty(difficulty)
But that low and high are never used in the banner. The fix is simple—use the variables instead:


st.info(
    f"Guess a number between {low} and {high}. "
    f"Attempts left: {attempt_limit - st.session_state.attempts}"
)
Want me to fix this?
```

I fixed this issue myself then tried going on to the next one but was typing as Claude was working. Led to some unintended issues so I stopped the tool and tried again.

>  Let's look again at the states for the bug on the history not changing. When I enter 50, i see no change to history. I add a new valuw, 51, and then 50 gets added to the history. But weirdly, after adding 52, 51 does not get added to the history.

```
That's a strange pattern! Let me trace through what's happening. Look at line 42 in check_guess:

This was changed from g = str(guess), but that might be creating an issue. On even attempts (line 158-159), the secret is converted to a string:

So when you submit on even attempt numbers, you're comparing an int guess against a str secret, which causes a TypeError. The except block then tries g = int(guess) — but guess is already an int, so that doesn't fix the string comparison. This should be:

Change that line:

Good news—line 42 is already correct with g = str(guess).

But the history pattern you're describing (50 added on 2nd submit, 51 not added on either 2nd or 3rd submit) suggests the issue is with raw_guess not being updated correctly between submissions.

A few clarifying questions:

After you submit 50 and it's not in history, does the text input still show "50", or is it cleared?
When you type 51, does it replace the 50, or are you clearing it first and then typing 51?
After the third submit (52), if you submit again with the text input unchanged, does anything get added to history?
The text input key is f"guess_input_{difficulty}" (line 123)—if difficulty is somehow changing between your submissions, that would reset the input to empty and cause the value to get mismatched. Are you changing the difficulty selector at all?
```

My responses were:

> 1) the text input shows 50.
> 2) i clear '50' and type '51'.
> 3) after i hit submit again for '52' (this would be submitting it for a second time), '52' gets added to the history, but 51 is not added.
---

Claude:
```
Aha! So the text input isn't being cleared after submit. That's the key insight. Let me trace through what's happening:

1. User types 50, submits → input still shows 50, history should be [50] but is []
2. User clears and types 51, submits → input shows 51, history is [50] (the first submit finally worked!)
3. User clears and types 52, submits first time → input shows 52, history is still [50]
4. User submits 52 again without changing it → history is [50, 52]

The issue is the text input isn't being cleared, so **the same value is being read multiple times**. Let me look at the text input creation and the submit handler:

Read [app.py](app.py)

I think I found it! After you submit, the text input value persists in Streamlit's session state under the key `guess_input_Normal` (or whatever difficulty). The problem is **the text input isn't being cleared**, so the old value stays in session state.

When you manually clear and type a new value in the browser, Streamlit should read the new value on the next rerun. But something's preventing it from being recognized as a new submission.

The fix is to **clear the text input after a successful submission**. Add this line after the history append (line 156):

```python
st.session_state[f"guess_input_{difficulty}"] = ""
```

This should go right after the history is appended, to clear the text input for the next submission. Try adding it and see if that fixes the issue.
```


sadly, this did not work as we wanted it to. I'm not the best web dev, so I'm not sure what I should do to fix it though. Hopefully Claude can help me fix this.

> no luck, history is not consistently updating for each submission. the text input isn't cleared on the "Submit Guess" button press either?

Claude:

```
This is getting stranger. Let me get some diagnostic info. Can you check the "Developer Debug Info" section at the bottom of the app and tell me what it shows for:

Attempts after each submission
History after each submission
Difficulty (are you staying on the same one?)
Also:

Are you seeing any error messages or warnings in red/orange?
After you clear the text input and type 51, does the app automatically rerun, or do you have to click Submit for anything to happen?
The off-by-one pattern suggests raw_guess might be stale or the script isn't executing the history append code on certain submissions. The debug info should reveal what's actually in the session state vs. what you expect.
```

> Attempts starts at 1 for a new game when it should be 0. I didn't notice that before. When submitting 50 for the first guess,

```
attempts: 1
Difficulty: Normal
History: []
```

> When submitting 51 for the first guess,

```
attempts: 2
Difficulty: Normal
History: [
0:50
]
```

> When submitting 51 for the second guess,

```
attempts: 2
Difficulty: Normal
History: [
0:50
]
```

> When submitting 52 for the third guess,

```
attempts: 2
Difficulty: Normal
History: [
0:50
]
```

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

| Edge Case | Prompt Used | AI-Suggested Test | Did It Pass? | Your Reasoning |
|-----------|-------------|-------------------|--------------|----------------|
| | | | | |
| | | | | |
| | | | | |

---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

**Prompt used:**

```
<!-- Paste the prompt you gave the AI -->
```

**Linting output before:**

```
<!-- Paste relevant linter warnings/errors -->
```

**Changes applied:**

<!-- Describe what you changed based on the AI's suggestions -->

---

## Model Comparison (SF11)

> Compare two AI models on the same task.

**Task given to both models:**

<!-- Describe what you asked each model to do -->

| | Model A | Model B |
|-|---------|---------|
| **Model name** | | |
| **Response summary** | | |
| **More Pythonic?** | | |
| **Clearer explanation?** | | |

**Which did you prefer and why?**

<!-- Your conclusion -->
