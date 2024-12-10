from main import second_function


def test_mocking_class_method(mocker):
    def mock_get_data(self):
        return {"field1": 100, "field2": 200}

    mocker.patch(
        'main.DataProvider.get_data',  # Мокируем get_data(),
        mock_get_data                  # импортируемую в main.py
    )

    data = second_function()
    assert data['field1'] == 100
    assert data['field2'] == 200
