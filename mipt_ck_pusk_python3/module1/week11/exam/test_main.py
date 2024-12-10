from main import caps

import pytest

def test_caps():
    assert caps("test") == "TEST"

def test_caps_on_non_string():
    with pytest.raises(TypeError):
        caps(1234)