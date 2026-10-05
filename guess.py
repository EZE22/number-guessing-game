import random
import time

# ---------- Settings ----------
DEBUG_SECRET = 42     # For testing, set to a number such as 42. Set back to None before your final commit.
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
# Same pattern as the level menu: show the choices, then keep asking until the answer is valid.
# timed is True or False. The rest of the game checks timed to decide whether to use the clock.
print("\nChoose a mode:")
print("1. Classic")
print(f"2. Time Challenge ({TIME_LIMIT} seconds)")

while True:
    mode_choice = input("Mode (1 or 2): ").strip()

    if mode_choice == "1":
        timed = False
        break
    elif mode_choice == "2":
        timed = True
        break
    else:
        print("Please type 1 or 2.")

# ---------- Set up the round ----------
# If DEBUG_SECRET has a number in it, use that number so tests are predictable.
# Otherwise, let the computer pick a random whole number from low to high.
if DEBUG_SECRET is not None:
    secret_number = DEBUG_SECRET
else:
    secret_number = random.randint(low, high)

# attempts_used counts only VALID guesses. It starts at 0 and goes up by 1 per valid guess.
attempts_used = 0

# result remembers how the round ended: "won", "lost" (out of attempts), or "timeout".
# We assume "lost" and change it when something else happens.
result = "lost"

# Save the start time ONCE, here, before the guess loop. If you saved it inside the loop,
# the clock would restart on every guess and the player would never run out of time.
# In Classic mode we save it too, but never use it.
start_time = time.time()

print(f"\nI picked a number from {low} to {high}. You have {max_attempts} attempts.")

# ---------- Guess loop ----------
# The loop stops on its own when attempts_used reaches max_attempts.
while attempts_used < max_attempts:
    # TIMER DISPLAY: shown before each guess, in Time Challenge mode only.
    # elapsed is how many seconds have passed since the round started.
    # round() gives a whole number. (int() would show 59 on the very first pass.)
    # max(0, ...) stops the display from ever going below zero.
    if timed:
        elapsed = time.time() - start_time
        seconds_left = max(0, round(TIME_LIMIT - elapsed))
        print(f"Time remaining: {seconds_left} seconds")

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

    # TIMEOUT CHECK: only after a valid guess, and BEFORE we look at whether it was correct.
    # That order is on purpose: if time ran out, even a correct guess does not count.
    # input() waits for the player, so this is the first moment we can notice the time is up.
    if timed and time.time() - start_time > TIME_LIMIT:
        result = "timeout"
        break

    # Compare the guess to the secret.
    if guess == secret_number:
        result = "won"
        print("\nCongratulations! You guessed the number!")
        break  # A correct guess ends the round right away.
    elif guess < secret_number:
        print("Too low.")
    else:
        print("Too high.")

    # Only reached after a wrong guess. Show how many attempts are left.
    attempts_left = max_attempts - attempts_used
    print(f"Attempts remaining: {attempts_left}")

# ---------- End of round ----------
# The loop can end three ways: a win, a timeout, or no attempts left.