import pytest
from Day16.math_ops import add, divide


def test_add_basic():
    assert add(2, 5) == 7


def test_divide_basic():
    assert divide(5, 2) == 2.5


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
