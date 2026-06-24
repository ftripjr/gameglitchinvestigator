from logic_utils import check_guess, get_range_for_difficulty, parse_guess, update_score

# check_guess tests
def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    # assert result == ("Win", "🎉 Correct!")
    assert result[0] == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    # assert result == ("Too High", "📉 Go LOWER!")
    assert result[0] == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    # assert result == ("Too Low", "📈 Go HIGHER!")
    assert result[0] == "Too Low"

# get_range_for_difficulty tests
def test_get_range_for_difficulty_easy():
    low, high = get_range_for_difficulty("Easy")
    assert low == 1
    assert high == 20


def test_get_range_for_difficulty_normal():
    low, high = get_range_for_difficulty("Normal")
    assert low == 1
    assert high == 50


def test_get_range_for_difficulty_hard():
    low, high = get_range_for_difficulty("Hard")
    assert low == 1
    assert high == 100


def test_get_range_for_difficulty_default():
    low, high = get_range_for_difficulty("Invalid")
    assert low == 1
    assert high == 50


def test_get_range_for_difficulty_none():
    low, high = get_range_for_difficulty(None)
    assert low == 1
    assert high == 50

# parse_guess tests
def test_parse_guess_valid_integer():
    ok, guess_int, err = parse_guess("50")
    assert ok is True
    assert guess_int == 50
    assert err is None


def test_parse_guess_valid_float():
    ok, guess_int, err = parse_guess("3.14")
    assert ok is True
    assert guess_int == 3
    assert err is None


def test_parse_guess_zero():
    ok, guess_int, err = parse_guess("0")
    assert ok is True
    assert guess_int == 0
    assert err is None


def test_parse_guess_negative():
    ok, guess_int, err = parse_guess("-10")
    assert ok is True
    assert guess_int == -10
    assert err is None


def test_parse_guess_none():
    ok, guess_int, err = parse_guess(None)
    assert ok is False
    assert guess_int is None
    assert err == "Enter a guess."


def test_parse_guess_empty_string():
    ok, guess_int, err = parse_guess("")
    assert ok is False
    assert guess_int is None
    assert err == "Enter a guess."


def test_parse_guess_non_numeric():
    ok, guess_int, err = parse_guess("abc")
    assert ok is False
    assert guess_int is None
    assert err == "That is not a number."

# update_score tests
def test_update_score_win_perfect():
    result = update_score(current_score=0, outcome="Win")
    assert result == 100


def test_update_score_win_with_penalties():
    result = update_score(current_score=-30, outcome="Win")
    assert result == 70


def test_update_score_win_near_floor():
    result = update_score(current_score=-95, outcome="Win")
    assert result == 10


def test_update_score_too_high():
    result = update_score(current_score=0, outcome="Too High")
    assert result == -5


def test_update_score_too_low():
    result = update_score(current_score=-10, outcome="Too Low")
    assert result == -15


def test_update_score_invalid_outcome():
    result = update_score(current_score=50, outcome="Invalid")
    assert result == 50