from main import fibonacci


def test_fibonacci_1():
    assert fibonacci(7) == 13


def test_fibonacci_2():
    assert fibonacci(-2) == 0
