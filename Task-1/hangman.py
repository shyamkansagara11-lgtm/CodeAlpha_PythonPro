import random

# Step 1: Predefined words
words = ["apple", "tiger", "chair", "robot", "plant"]

# Step 2: Choose random word
word = random.choice(words)
guessed_letters = []
wrong_guesses = 0
max_wrong = 6

# Step 3: Game loop
while wrong_guesses < max_wrong:
    display = ""

    # Show current progress
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    # Check win condition
    if "_" not in display:
        print("🎉 You Win!")
        break

    # Take input
    guess = input("Enter a letter: ").lower()

    # Check input
    if guess in guessed_letters:
        print("Already guessed!")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Correct guess!")
    else:
        wrong_guesses += 1
        print("❌ Wrong guess! Attempts left:", max_wrong - wrong_guesses)

# Step 4: Lose condition
if wrong_guesses == max_wrong:
    print("💀 You Lose! The word was:", word)