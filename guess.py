import random
import time

# ---------- Settings ----------
DEBUG_SECRET = None     # For testing, set to a number such as 42. Set back to None before your final commit.
TIME_LIMIT = 60       # Seconds allowed in Time Challenge mode

print("\n!!!Welcome to the Number Guessing Game!!!")

# ---------- Choose a level ----------
# Show the menu, then keep asking until the player types 1, 2, or 3.
# The chosen level sets three values: low, high, and max_attempts.
print("\nChoose a level:")
print("1. Easy   (1 to 50, 10 attempts)")
print("2. Medium (1 to 100, 8 attempts)")
print("3. Hard   (1 to 500, 10 attempts)")

while True:
    level_choice = input("\nLevel (1, 2, or 3): ").strip()

    # Compare the text to each valid answer. The choice is text, so we compare to "1", not 1.
    if level_choice == "1":
        low = 1
        high = 50
        max_attempts = 10
        break  # Valid choice, so leave the menu loop.
    elif level_choice == "2":
        low = 1
        high = 100
        max_attempts = 8
        break
    elif level_choice == "3":
        low = 1
        high = 500
        max_attempts = 10
        break
    else:
        # Anything else (blank, letters, 4, and so on) lands here. The loop repeats and asks again.
        print("Please type 1, 2, or 3.")

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

# result remembers how the round ended. We assume "lost" and change it to "won" on a correct guess.
# Remembering this is what lets the end of the game print the right message exactly once.
result = "lost"

print(f"\nI picked a number from {low} to {high}. You have {max_attempts} attempts.")

# ---------- Guess loop ----------
# The loop now stops on its own when attempts_used reaches max_attempts.
while attempts_used < max_attempts:
    # Ask for a guess. strip() removes any spaces the player typed before or after the text.
    guess_text = input("\nYour guess: ").strip()

    # CHECK 1: blank entry.
    if guess_text == "":
        print("You typed nothing. Please enter a number.")
        continue  # Back to the top of the loop. attempts_used does not change.

    # CHECK 2: letters or symbols. Must come BEFORE int(), because int("abc") would crash.
    if not guess_text.isdigit():
        print("That is not a whole number. Please enter digits only.")
        continue

    # Safe to convert now, because we know the text is all digits.
    guess = int(guess_text)

    # CHECK 3: outside the range for the chosen level.
    if guess < low or guess > high:
        print(f"Out of range. Please enter a number from {low} to {high}.")
        continue

    # The guess is valid, so it counts as an attempt.
    attempts_used = attempts_used + 1

    # Compare the guess to the secret.
    if guess == secret_number:
        result = "won"
        break  # A correct guess ends the round right away.
    elif guess < secret_number:
        print("Too low.")
    else:
        print("Too high.")

    # Only reached after a wrong guess. Show how many attempts are left.
    attempts_left = max_attempts - attempts_used
    print(f"Attempts remaining: {attempts_left}")

# ---------- End of round ----------
# The loop ends in one of two ways right now: a win (break) or no attempts left.
# result tells us which, so we print exactly one message.
if result == "won":
    print(f"Correct! You got it in {attempts_used} attempts.")
else:
    print(f"Out of attempts. The secret number was {secret_number}.")