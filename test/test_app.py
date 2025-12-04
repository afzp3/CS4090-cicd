from src.app import add
from pathlib import pathlib

root = Path(__file__.resolve().parents[1])
sys.path.insert(0, str(root / "src"))

def test_add():
    assert add(5, 6) == 11

def test_add2():
    assert add(5, 6) != 10