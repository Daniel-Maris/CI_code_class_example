import pytest
from mymath import my_power, my_root


def test_power():
    assert my_power(2, 3) == 8


def test_root():
    assert my_root(9, 2) == 3


def test_invalid_input_root():
    with pytest.raises(TypeError):
        my_root(16,"squareroot")
    with pytest.raises(ZeroDivisionError):
        my_root(16,0)
        