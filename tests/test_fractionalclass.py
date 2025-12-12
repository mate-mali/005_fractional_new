from fractional_new.FractionalClass import Fractional
 
#TODO: pytest runs when called from the root folder 

x1 = Fractional(1, 4)
x2 = Fractional(2, 3)

def test_fractional_add():
    assert x1 + x2 == Fractional(11, 12)
    
def test_fractional_sub():
    assert x1 - x2 == Fractional(-5, 12)
    
def test_fractional_mul():
    assert x1 * x2 == Fractional(2, 12)
    
def test_fractional_div():
    assert x1 / x2 == Fractional(3, 8)
    assert x2 / x1 == Fractional(8, 3)
    
def test_fractional_div():
    assert x1 / x2 == Fractional(3, 8)
    assert x2 / x1 == Fractional(8, 3)   

def test_fractional_gt_lt():
    assert (x1 < x2) == True
    assert (x1 > x2) == False
    
def test_fractional_gte_lte():
    assert (x1 <= x2) == True
    assert (x2 >= x2) == True
    
def test_integer_fract():
    assert 1 + x1 == Fractional(5,4)
    assert x1 + 1 == Fractional(5,4)

