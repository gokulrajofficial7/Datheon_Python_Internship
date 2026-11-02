"""
Datheon Python Programming Internship - Task 1
Hangman Word Guessing Game (Console)

Features:
- Dynamic ASCII gallows visual stage art (0 to 6 incorrect attempts)
- Random secret word selection from 'words.txt' or fallback wordlist
- Tracks guessed letters to prevent duplicate penalty deductions
- Clean formatted victory/defeat terminal screens with replay support
"""

import os
import random
import sys

# ASCII Stages representing the Hangman state (0 mistakes to 6 mistakes)
HANGMAN_STAGES = [
    """
       +---+
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """
]

FALLBACK_WORDS = [
    "python", "developer", "algorithm", "database", "software",
    "variable", "function", "iteration", "framework", "automation",
    "artificial", "intelligence", "architecture", "technology", "engineering"
]

MAX_ATTEMPTS = 6


def load_words(filename="words.txt"):
    """Loads word list from an external text file, or returns fallbacks if not found."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, filename)
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            words = [line.strip().lower() for line in f if len(line.strip()) >= 4]
            if words:
                return words
    return FALLBACK_WORDS


def get_masked_word(secret_word, guessed_letters):
    """Returns the secret word masked with underscores for unrevealed letters."""
    return " ".join([letter.upper() if letter in guessed_letters else "_" for letter in secret_word])


def play_game():
    """Runs a single round of the Hangman game."""
    words = load_words()
    secret_word = random.choice(words).lower()
    guessed_letters = set()
    incorrect_guesses = set()
    mistakes = 0

    print("\n" + "=" * 60)
    print("      DATHEON - HANGMAN WORD GUESSING TERMINAL GAME        ")
    print("=" * 60)
    print(f"I have picked a secret word with {len(secret_word)} letters. Can you guess it?")

    while mistakes < MAX_ATTEMPTS:
        print(HANGMAN_STAGES[mistakes])
        print(f"Word: {get_masked_word(secret_word, guessed_letters)}")
        print(f"Attempts Remaining: {MAX_ATTEMPTS - mistakes} | Incorrect Guesses: {', '.join(sorted(incorrect_guesses)).upper() or 'None'}")
        
        try:
            guess = input("\nEnter your guess (single letter): ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("\nGame session ended.")
            return False

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("[Warning] Invalid input. Please enter a single alphabetic letter (a-z).")
            continue

        if guess in guessed_letters or guess in incorrect_guesses:
            print(f"[Notice] You already guessed '{guess.upper()}'. No penalty incurred.")
            continue

        # Check guess correctness
        if guess in secret_word:
            guessed_letters.add(guess)
            print(f"[Good Job!] '{guess.upper()}' is in the secret word!")
            # Check for victory
            if all(letter in guessed_letters for letter in secret_word):
                print(HANGMAN_STAGES[mistakes])
                print("\n" + "*" * 60)
                print(f"🎉 VICTORY! You guessed the secret word: '{secret_word.upper()}'!")
                print("*" * 60)
                return True
        else:
            incorrect_guesses.add(guess)
            mistakes += 1
            print(f"[Oops!] '{guess.upper()}' is NOT in the secret word.")

    # Defeat state
    print(HANGMAN_STAGES[MAX_ATTEMPTS])
    print("\n" + "!" * 60)
    print(f"💀 GAME OVER! You ran out of attempts.")
    print(f"The secret word was: '{secret_word.upper()}'")
    print("!" * 60)
    return False


def main():
    while True:
        play_game()
        try:
            choice = input("\nWould you like to play another round? (y/n): ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            break
        if choice not in ('y', 'yes'):
            print("\nThank you for playing Hangman! Happy Coding with Datheon.")
            break


if __name__ == "__main__":
    main()
