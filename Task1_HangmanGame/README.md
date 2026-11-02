# Task 1: Hangman Word Guessing Game (Console)

## Overview
An interactive, modular terminal-based Hangman game built with Python 3 implementing string manipulation, sets for tracking guessed states, input validation, and dynamic ASCII gallows visual art.

---

## 🛠️ Key Features
- **Visual ASCII Art Stages:** 7 progressive gallows stages corresponding to 0 through 6 mistakes.
- **Word Bank:** Loads words from an external `words.txt` or falls back to an internal curated list.
- **Set-Based Duplicate Protection:** Tracks both correct and incorrect letters in sets, preventing duplicate penalty deduction if a player enters an already guessed letter.
- **Robust Input Validation:** Rejects non-alphabetic characters and multi-character inputs with helpful user feedback.

---

## 🚀 How to Run
```bash
python hangman.py
```
