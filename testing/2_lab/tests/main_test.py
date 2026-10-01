from lab.main import validate_score

def validate_score_test_new():
    # Цей тест не буде виконуватися автоматично
    assert validate_score(10) is True, "Повинен впасти з помилкою"

def validate_score_valid_test():
    # тест закінчується на _test і не буде виконуватися автоматично
    for score in [0, 10, 50, 100]:
        assert validate_score(score) is None, f"Expected None for valid score {score}"

def test_1():
    assert True, "Цей тест буде виконуватися автоматично"
