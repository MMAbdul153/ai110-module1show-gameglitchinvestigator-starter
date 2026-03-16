# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] Describe the game's purpose.

  A number guessing game where the player tries to guess a secret number within a limited number of attempts. The difficulty setting controls the number range and attempt limit. Points are awarded based on how quickly the correct number is guessed.

- [x] Detail which bugs you found.

  1. **Wrong hint directions** — "Too High" told the player to go higher, and "Too Low" told them to go lower, making it impossible to win by following the hints.
  2. **String/int type mismatch** — On every even-numbered attempt, the secret was passed as a string, causing incorrect comparisons against the integer guess.
  3. **New Game button broken** — Clicking "New Game" after a win or loss didn't reset `status`, so the game immediately stopped again. It also didn't clear the guess history, and always picked a new secret from 1–100 regardless of difficulty.
  4. **Logic not separated** — All game logic lived in `app.py` with no tests, making bugs hard to catch.

- [x] Explain what fixes you applied.

  1. Fixed the hint messages in `check_guess` so "Too High" maps to "Go LOWER" and "Too Low" maps to "Go HIGHER".
  2. Added `int()` conversion for both `guess` and `secret` in `check_guess` to eliminate type mismatch errors.
  3. Fixed the New Game button to reset `status`, `history`, and use the difficulty-aware range for the new secret.
  4. Refactored all logic functions into `logic_utils.py` and fixed the test suite so `pytest` passes.

## 📸 Demo

- [ ] [Insert a screenshot of your fixed, winning game here]

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
