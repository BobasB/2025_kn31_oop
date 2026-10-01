from lab.main import validate_score

def test_validate_score_valid():
    # тест починається з test_ і буде виконуватися автоматично
    for score in [0, 10, 50, 100]:
        assert validate_score(score) is None, f"Expected None for valid score {score}"

