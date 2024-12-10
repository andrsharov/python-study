import pytest
from main import first_function


@pytest.fixture
def lucky_numbers():
    return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_first_function(mocker, lucky_numbers):
    mocker.patch(
        'main.get_lucky_number',  # Мокируем get_lucky_number(),
        return_value=5            # импортируемую в main.py
    )

    lucky_number = first_function()
    assert lucky_number in lucky_numbers  # [1, 2, ..., 10] из фикстуры
