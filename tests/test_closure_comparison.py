from main import closure_comparison


def test_closure_comparison_1():
    a = closure_comparison('>')
    assert a(2, 5) == False


def test_closure_comparison_2():
    a = closure_comparison('>')
    assert a(5, 2) == True
