from fractional_new.FractionalClass import Fractional
 
#TODO: cannot currently make tests wotk from pytest running from inside .venv


def test_create():
    x1 = Fractional(1, 4)
    x2 = Fractional(2, 3)
    assert x1 + x2 == Fractional(11, 12)
    assert x1 - x2 == Fractional(-5, 12)
    assert x1 * x2 == Fractional(2, 12)
    assert x1 / x2 == Fractional(3, 8)
    assert x2 / x1 == Fractional(8, 3)
    print("done")

def test_():
    x1 = Fractional(1, 4)
    x2 = Fractional(2, 3)
    assert x1 + x2 == Fractional(11, 12)
    assert x1 - x2 == Fractional(-5, 12)
    assert x1 * x2 == Fractional(2, 12)
    assert x1 / x2 == Fractional(3, 8)
    assert x2 / x1 == Fractional(8, 3)
    print("done")

def test_Fractional():
    x1 = Fractional(1, 4)
    x2 = Fractional(2, 3)
    assert x1 + x2 == Fractional(11, 12)
    assert x1 - x2 == Fractional(-5, 12)
    assert x1 * x2 == Fractional(2, 12)
    assert x1 / x2 == Fractional(3, 8)
    assert x2 / x1 == Fractional(8, 3)
    print("done")

if __name__ == '__main__':
    test_create()
