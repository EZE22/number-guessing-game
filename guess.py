import random
import time

# ---------- Settings ----------
DEBUG_SECRET = None     # For testing, set to a number such as 42. Set back to None before your final commit.
TIME_LIMIT = 60       # Seconds allowed in Time Challenge mode

print("\n!!!Welcome to the Number Guessing Game!!!")

# ---------- Choose a level ----------
# Classic mode only for now: one fixed range. The level menu comes on the next branch.
low = 1
high = 100

# ---------- Choose a mode ----------
# Not built yet. The mode menu comes on the time-challenge branch.

# ---------- Set up the round ----------
# If DEBUG_SECRET has a number in it, use that number so tests are predictable.
# Otherwise, let the computer pick a random whole number from low to high.
if DEBUG_SECRET is not None:
    secret_number = DEBUG_SECRET
else:
    secret_number = random.randint(low, high)

# attempts_used counts only VALID guesses. It starts at 0 and goes up by 1 per valid guess.
attempts_used = 0

print(f"\nI picked a number from {low} to {high}. Can you guess it?")

# ---------- Guess loop ----------
# while True means "repeat forever". The only way out is a break statement.
while True:
    # Ask for a guess. strip() removes any spaces the player typed before or after the text.
    guess_text = input("\nYour guess: ").strip()


    # CHECK 1: blank entry. An empty string is "", so this catches a player who just pressed Enter.
    if guess_text == "":
        print("You typed nothing. Please enter a number.")
        continue  # Go back to the top of the loop. attempts_used does not change.

    # CHECK 2: letters or symbols. isdigit() is True only when every character is a digit.
    # We must check this BEFORE int(), because int("abc") would crash the program.
    if not guess_text.isdigit():
        print("That is not a whole number. Please enter digits only.")
        continue

    # Safe to convert now, because we know the text is all digits.
    guess = int(guess_text)

    # CHECK 3: outside the range. Negative numbers never reach here (the "-" fails isdigit).
    if guess < low or guess > high:
        print(f"Out of range. Please enter a number from {low} to {high}.")
        continue

    # If we get here, the guess is valid, so it counts as an attempt.
    attempts_used = attempts_used + 1

    # Compare the guess to the secret and give a hint.
    if guess < secret_number:
        print("Too low.")
    elif guess > secret_number:
        print("Too high.")
    else:
        # Correct guess. Show the attempt count and leave the loop.
        print(f"Correct! You got it in {attempts_used} attempts.")
        break

# ---------- End of round ----------
# Nothing else to do yet. Later branches add the loss and timeout messages here.