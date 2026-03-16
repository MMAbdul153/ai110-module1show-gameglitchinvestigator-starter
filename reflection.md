# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?
While playing the game for the first time, the hints seem misleading. When I choose a number higher than the secret number, the hint says to go even higher, which is misleading; you would expect it to tell you to go lower, which is more helpful for finding the secret number. Likewise, when it was lower, it said to go even lower, which is also misleading.
After winning a game, the game doesn't start a new game when you click the new game button.

---

## 2. How did you use AI as a teammate?

I used Gemini and Claude Code. 

Gemini explained the logic of the check_guess function and explained that the logic doesn't follow correct mathematical logical where the hint given should properly guide the user to the correct answer. If guess is higher, hint should say "Go lower", and if guess is "lower", hint should say "Go Higher". It suggests just swapping the strings from both statements to easily correct that logic. 
It also pointed out that comparing strings using '<' and '>' can be problematic because '10' > '2' returns False, whereas mathematically we would expect it to return True. Therefore, we should tackle this issue by ensuring that the guess and secret are cast as integers first. It also suggested using a simple if-else statement to correct this logic. 



---

## 3. Debugging and testing your fixes

I decided a bug was fixed when both the manual test (playing the game and following the hints) and the automated pytest tests all passed. For example, after swapping the hint strings in `check_guess`, I played through a round and confirmed the hints now correctly guided me toward the secret number.

I ran `pytest tests/test_game_logic.py` after refactoring the logic into `logic_utils.py`. Initially the tests failed because the assertions compared the full tuple returned by `check_guess` to a plain string — for example, `("Win", "🎉 Correct!") == "Win"` is always `False`. Fixing the assertions to use `result[0]` made the intent of each test clear and they all passed.

Claude Code helped me understand why the tests were failing by explaining that `check_guess` returns a tuple, not a string, and suggested using `result[0]` to check just the outcome. It also suggested adding tests specifically for the string/int type mismatch case, which directly matched the bug that was introduced on even-numbered attempts.

---

## 4. What did you learn about Streamlit and state?

In the original app, the secret number was assigned with `st.session_state.secret = random.randint(...)` outside of a `if "secret" not in st.session_state` guard, so every time the user clicked a button, Streamlit re-ran the entire script from top to bottom and generated a new random number.

Streamlit works by re-executing your entire Python script on every user interaction — clicking a button, typing in a box, anything. `session_state` is like a dictionary that survives these reruns, so values stored there stay the same across interactions instead of being reset.

The fix was wrapping the secret assignment in `if "secret" not in st.session_state:`, so it only generates a new number when the key doesn't already exist — meaning it runs once at the start and then holds its value across all reruns.

---

## 5. Looking ahead: your developer habits

One habit I want to carry forward is writing tests alongside the logic, not after. Having `pytest` catch the tuple assertion mistake immediately showed me how much time automated tests save compared to only relying on manual play-testing.

Next time I work with AI on a coding task, I would ask it to explain *why* a fix works, not just what to change — understanding the reason (e.g. why string comparison of numbers is unreliable) helps me spot the same class of bug in future code.

This project changed the way I think about AI-generated code because it showed me that AI can produce code that looks correct and complete at first glance but contains subtle logical errors that only surface when you actually use it. Reviewing and testing AI output is just as important as reviewing code written by a human.
