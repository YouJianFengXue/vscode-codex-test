import pytest

from src.calc import add, div


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (0, 0, 0),
        (1, 2, 3),
        (-1, 1, 0),
        (2.5, 3.5, 6.0),
    ],
)
def test_add(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (4, 2, 2),
        (3, 2, 1.5),
        (-6, 3, -2),
    ],
)
def test_div(a, b, expected):
    assert div(a, b) == expected


def test_div_by_zero():
    with pytest.raises(ZeroDivisionError):
        div(1, 0)

