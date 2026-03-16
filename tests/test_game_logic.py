from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result[0] == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result[0] == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result[0] == "Too Low"

# Tests for the string/int type mismatch bug fix:
# app.py passes secret as a string on even attempts, so check_guess
# must handle mixed types without incorrect comparisons.

def test_winning_guess_with_string_secret():
    # secret passed as string (as app.py does on even attempts)
    result = check_guess(50, "50")
    assert result[0] == "Win"

def test_too_high_with_string_secret():
    # Without the int() fix, string comparison "60" > "50" could misbehave
    result = check_guess(60, "50")
    assert result[0] == "Too High"

def test_too_low_with_string_secret():
    result = check_guess(40, "50")
    assert result[0] == "Too Low"
