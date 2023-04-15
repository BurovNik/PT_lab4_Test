from main import closure_del_str


def test_closure_del_str_1():
    a = closure_del_str('Test string')
    assert a('s') == 'Tet tring'


def test_closure_del_str_2():
    a = closure_del_str('Test string')
    assert a('t') == 'Tes sring'

