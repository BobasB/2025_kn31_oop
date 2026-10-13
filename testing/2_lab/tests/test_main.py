import pytest

from lab.main import validate_score


@pytest.mark.unit
@pytest.mark.score_validation
@pytest.mark.main_testing
@pytest.mark.parametrize("score", [[0, 10, 50, 100], [20, 60, 100]])
def test_validate_score_valid(score):
    # тест починається з test_ і буде виконуватися автоматично
    for s in score:
        assert validate_score(s) is None, f"Expected None for valid score {s}"
