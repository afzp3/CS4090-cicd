import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))


from app import add, sub, mult, div, squared
import pytest

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
    assert div(x, y) == expected

@pytest.mark.parametrize("a", [1, 2, 3, 4, 5])
def test_squared(a):
    assert squared(a) == mult(a, a)