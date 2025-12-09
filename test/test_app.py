import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))

from app import add, sub, mult, div, squared, log, sin, cos, percentage, squareroot
import pytest
from math import sqrt, log, sin, cos

def test_add():
    assert add(5, 6) == 11

def test_add2():
    assert add(5, 6) != 10

def test_sub1():
    assert sub(6, 5) == -sub(5, 6)

def test_sub2():
    assert sub(10, 10) == 0

@pytest.mark.parametrize("a", [1, 2, 3, 4, 5])
def test_mult_identity(a):
    assert mult(a, 1) == a

@pytest.mark.parametrize("x,y", [(1, 2), (2, 3), (3, 4), (4, 5), (5, 0)])
def test_mult_commutative(x, y):
    assert mult(x, y) == mult(y, x)

@pytest.mark.parametrize(
    "x,y,expected",
    [
        (10,1,10),
        (1.2,2,0.6),
        (-1,0,ZeroDivisionError)
    ]
)
def test_div(x,y,expected):
    if expected == ZeroDivisionError:
        with pytest.raises(ZeroDivisionError):
            div(x,y)
    else:
        assert div(x, y) == expected

@pytest.mark.parametrize("a", [1, 2, 3, 4, 5])
def test_squared(a):
    assert squared(a) == mult(a, a)

@pytest.mark.parametrize("base", [2, 3, 4, 5])
def test_log1(base):
    # log rule: log_b(1) = 0
    assert log(1, base) == 0

@pytest.mark.parametrize("base", [2, 3, 4, 5])
def test_log2(base):
    # log rule: log_b(b) = 1
    assert log(base, base) == 1

@pytest.mark.parametrize("a", [1, 2, 3, 4, 5])
def test_sin(a):
    assert sin(a) >= -1 and sin(a) <= 1

@pytest.mark.parametrize("a", [1, 2, 3, 4, 5])
def test_cos(a):
    assert cos(a) >= -1 and cos(a) <= 1

@pytest.mark.parametrize(
    "x,y,expected",
    [
        (1,10,10),
        (6,6,100),
        (1,0,ValueError)
    ]
)
def test_percentage(x, y, expected):
    if expected == ValueError:
        with pytest.raises(ValueError):
            percentage(x, y)
    else:
        assert percentage(x, y) == expected

@pytest.mark.parametrize(
    "x,expected",
    [
        (49,7),
        (36,6),
        (0, 0),
        (-1,ValueError)
    ]
)
def test_squareroot(x, expected):
    if expected == ValueError:
        with pytest.raises(ValueError):
            squareroot(x)
    else:
        assert squareroot(x) == expected