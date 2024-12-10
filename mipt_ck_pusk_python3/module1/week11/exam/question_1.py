import pytest

def caps(s: str) -> str:
    if type(s) != str:
        raise TypeError('На входе ожидалась строка')
    return s.upper()

def test_caps():
    assert caps("test") == "TEST"

def test_caps_on_non_string():
    with pytest.raises(TypeError):
        caps(1234)