from src.math_operations import add, sub, mul, div

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_sub():
    assert sub(9, 5) == 4
    assert sub(-1, -8) == 7
    assert sub(10, -5) == 15

def test_mul():
    assert mul(4, 5) == 20
    assert mul(-2, 3) == -6
    assert mul(0, 100) == 0

def test_div():
    assert div(10, 2) == 5
    assert div(-9, 3) == -3
    assert div(7, -1) == -7

    try:
        div(5, 0)
    except ValueError as e:
        assert str(e) == "Cannot divide by zero"