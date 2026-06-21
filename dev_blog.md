# Game Glitch Investigator Dev Blog

## Blog 1 - Glitch Hunt

"Let's go hunt some Glitches?"
~ [Ekko buying Glitch Bane, LoL](https://leagueoflegends.fandom.com/wiki/Ekko/LoL/Audio)

### Test 1

After fixing some issues I had in the setup (dependencies were breaking in my local machine), I run the app and open up the Developer Debug Info to make sure my starting state is what I expect.

What I Expect to See:

- Secret: Between 1 and 100 (inclusive bounds)
- Difficulty: Normal
- Attempts: 0
- Attempts Remaining: 8
- Score: 0
- History: (empty)

What I Actually Saw:

- [x] Secret: Between 1 and 100 (inclusive of both bounds)
- [x] Difficulty: Normal
- [ ] Attempts: 1
- [ ] Attempts Remaining: 7
- [x] Score: 0
- [x] History: (empty)

So on app startup, we have attempts being incorrect. Not a good look. Let's see what I can do to fix it. Maybe restarting the app will reset the attempts to the correct values. I also want an easy test to run so I'll change the Difficulty to Easy, so I expect to have a secret between 1 and 20 (inclusive) in addition to the correction of the attempts and attempts remaining counts.  

What I Expect to See:

- Secret: Between 1 and 20 (inclusive bounds)
- Difficulty: Easy
- Attempts: 0
- Attempts Remaining: 6
- Score: 0
- History: (empty)

The following shows what appeared in the dev logs after clicking the New Game Button.

What I Actually Saw:

- [ ] Secret: 56 (greater than established bounds)
- [x] Difficulty: Easy
- [x] Attempts: 0
- [x] Attempts Remaining: 6
- [x] Score: 0
- [x] History: (empty)

I'll try clicking it again without changing anything.

- Secret: 56 (STILL greater than established bounds)

The new game button does not appear to properly create a easy new games. What about Hard?

- Secret: Between 1 and 50 (inclusive bounds)
- Difficulty: Hard
- Attempts: 0
- Attempts Remaining: 5
- Score: 0
- History: (empty)

- [x] Secret: 18 (Appears to be a Valid option)
- [x] Attempts: 0
- [x] Attempts Remaining: 5
- [x] Score: 0
- [x] Difficulty: Hard
- [x] History: (empty)

Though the dev tools are showing some changes that are in line with a new game, the banner text has not correctly updated the range the user should be guessing based on the difficulty.

Enough pre game testing. Let's go back to normal and try to guess the right answer in 5 guesses.

`NOTE: I will be cheating by using the hints and dev debug info box.`

Restarting the app, we have a normal game where the winning number is `33`. Let's see if we can use binary searching to get to our answer.

I input a guess of 50, press the Enter key, and expect "Too High" as the hint.

Pressing the enter key did nothing...

I'll press the submit guess button, then.

```js
Hint says: `📈 Go HIGHER!`
```

The game lies! But we'll go with it. Let's `Submit guess` of `75`, since the key is "higher".

There is no hint, and the history updates with the first guess, but doesn't read `75` at all. I'll submit it again.

```js
Hint: `📈 Go HIGHER!`
History: [
    0: 50
    ]
```

Still no `75` in the history. I'll try `100` to rule out the max value.

```js
Hint: `📉 Go LOWER!`
History: [
  0:50
  1:75
]
```

So updating of the history is not working as expected, but the Hint does correctly say go down this time. Maybe because you can't go any higher than the max?

We'll enter the key to see if we can win. Submit Guess of `33`.

```js
🎉 Correct!
History: [
  0: 50
  1: 75
  2: 100
]

You won! The secret was 33. Final score: 35
```

I didn't check how the score was calculated at all. I'll pay closer attention to how that is calculated.

Let's change the difficulty to easy and click New Game to get a new secret ready for the next run.

After the game ends and I try to change the difficulty, I got an error and warning on clicking the Difficulty dropdown.

```js
    // Error on click of dropdown arrow
    inject.js:254 Uncaught TypeError: e.target.className.indexOf is not a function
        at HTMLDocument.mouseup (inject.js:254:67)
    mouseup @ inject.js:254
```

```js
    // Warning on hover difficulty options
    index.dkY5s53S.js:25 
    `preventOverflow` modifier is required by `hide` modifier in order to work, be sure to include it before `hide`
```

After I select `Easy`. the `You won! The secret was 33. Final score: 35` banner changes to `You already won. Start a new game to play again.`.

Clicking the new game button doesn't start a new game anymore either.

Pretty Notable bugs in the first run.

### Test 2 - Easy Run with 1 Lucky Guess

With this run, I want to get a perfect score - I'm guessing `100` - so we'll restart the app and guess the secret to see what the score is and if we get the same error and warning for trying to create a new game.

- Input: Guess of `46` (Secret value: `46`)

- Expected:

```js
🎉 Correct!
History: [
    0: 46
    ]

You won! The secret was 46. Final score: 100
```

Actual:

```js

You won! The secret was 46. Final score: 70
```

And once again, trying to change the difficulty for a new game gave the following error, warning, and alert message displayed in the console and web app.

## Test 3 - The Quest for a 100, Part 2

Reset the app. Changed the difficulty from normal to easy and noticed the warnings showed up again! There's something wrong in that dropdown logic.

Anyway, new easy game. What's our secret? 

`69`

Not easy at all...

Final score of `80`, too. So there must be something wrong with the scoring system as well. Getting the scroe correct on attempt 1 should be a perfect for all levels. 

Found a good amount of bugs to test.

- [ ] on app startup, we have attempts being incorrect
- [ ] new game button does not appear to properly create new games
- [ ] Hints lie
- [ ] Banner for attempts and range based on difficulty does not update
- [ ] History doesn't properly update on guess submission
- [ ] Score System is bugged.
