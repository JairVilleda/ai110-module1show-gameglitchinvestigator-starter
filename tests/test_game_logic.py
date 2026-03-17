from logic_utils import check_guess, get_range_for_difficulty

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

#FIX: added new pytest test with Claude's guidance to verify check_guess logic and difficulty ranges
def test_check_guess_hints():
    # Guess lower than secret should return "Too Low" with "Go HIGHER!" hint
    assert check_guess(30, 50) == ("Too Low", "📈 Go HIGHER!")
    # Guess higher than secret should return "Too High" with "Go LOWER!" hint
    assert check_guess(70, 50) == ("Too High", "📉 Go LOWER!")
    # Guess equal to secret should return "Win" with "Correct!" hint
    assert check_guess(50, 50) == ("Win", "🎉 Correct!")

def test_difficulty_ranges():
    assert get_range_for_difficulty("Easy") == (1, 20)
    assert get_range_for_difficulty("Normal") == (1, 100)
    assert get_range_for_difficulty("Hard") == (1, 50)
