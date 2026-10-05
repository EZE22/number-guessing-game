# Number Guessing Game

A terminal number guessing game written in Python. The computer picks a secret number, and you guess it with "too low" and "too high" hints. You choose a difficulty level (Easy, Medium, or Hard) and a mode (Classic or Time Challenge).

## How to run the game in PyCharm

1. Open the `number-guessing-game` folder in PyCharm (File > Open).
2. Make sure the interpreter is the project's `.venv` (Python 3.12). It shows in the bottom right of the window.
3. Open `guess.py` and click the green Run button.
4. Click inside the Run window at the bottom, then type your answers and press Enter.
5. To play again, click the Rerun button in the Run window.

## Levels and modes

| Level | Range | Attempts allowed |
| ----- | ----- | ---------------- |
| Easy | 1 to 50 | 10 |
| Medium | 1 to 100 | 8 |
| Hard | 1 to 500 | 10 |

- **Classic:** no time limit.
- **Time Challenge:** 60 seconds for the whole round. The attempt limit still applies. The clock is checked after each valid guess, so a late guess ends the round even if it is correct.

## Settings

The settings are at the top of `guess.py`:

- `DEBUG_SECRET`: `None` for a random number, or a number such as 42 for testing.
- `TIME_LIMIT`: seconds allowed in Time Challenge mode (60 in the finished game).

## Test Plan

For these tests, `DEBUG_SECRET` was set to 42. For the Time Challenge tests, `TIME_LIMIT` was set to 5 so a timeout was quick to test. Both were set back to `None` and 60 before the final commit.

| # | What I tested | What I did | Expected result | Actual result | Pass? |
| - | ------------- | ---------- | --------------- | ------------- | ----- |
| 1 | Guess below the secret | Easy, Classic. Guessed 10 | Says too low | Said "Too low." and "Attempts remaining: 9" | Yes |
| 2 | Guess above the secret | Easy, Classic. Guessed 50 | Says too high | Said "Too high." and "Attempts remaining: 8" | Yes |
| 3 | Correct guess and attempt count | Easy, Classic. Guessed 10, 50, then 42 | Says correct and shows 3 attempts | Said "Correct! You got it in 3 attempts." | Yes |
| 4 | Letters as input | Typed abc as a guess | Rejected, attempt not counted | Said "That is not a whole number." The next valid guess still showed 9 attempts remaining | Yes |
| 5 | Blank input | Pressed Enter with nothing typed | Rejected, attempt not counted | Said "You typed nothing." Attempts did not change | Yes |
| 6 | Number below the range | Typed 0 on Easy | Rejected, attempt not counted | Said "Out of range. Please enter a number from 1 to 50." Attempts did not change | Yes |
| 7 | Number above the range | Typed 51 on Easy | Rejected, attempt not counted | Said "Out of range. Please enter a number from 1 to 50." Attempts did not change | Yes |
| 8 | Easy level settings | Chose level 1 | Range 1 to 50 and 10 attempts | Showed "I picked a number from 1 to 50. You have 10 attempts." | Yes |
| 9 | Medium level settings | Chose level 2 | Range 1 to 100 and 8 attempts | Showed "I picked a number from 1 to 100. You have 8 attempts." | Yes |
| 10 | Hard level settings | Chose level 3 | Range 1 to 500 and 10 attempts | Showed "I picked a number from 1 to 500. You have 10 attempts." | Yes |
| 11 | Running out of attempts | Medium, Classic. Guessed 1 through 8 | Game ends and reveals the number | Showed "Attempts remaining: 0", then "Out of attempts. The secret number was 42." | Yes |
| 12 | Invalid level and mode choices | Typed x at the level menu and y at the mode menu | Each menu asks again | Said "Please type 1, 2, or 3." and "Please type 1 or 2." and asked again | Yes |
| 13 | Remaining time shown | Easy, Time Challenge. Made two guesses | Seconds remaining shown before each guess | Showed "Time remaining: 5 seconds" before each guess | Yes |
| 14 | Timeout with a correct guess | Easy, Time Challenge. Guessed 10, waited 6 seconds, then guessed 42 | Game ends and reveals the number | Said "Time is up! The secret number was 42." even though 42 was correct | Yes |
| 15 | Classic mode has no timer | Easy, Classic. Made a guess | No time lines shown | No "Time remaining" lines appeared | Yes |