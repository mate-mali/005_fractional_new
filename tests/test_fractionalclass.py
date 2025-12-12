from fractional_new.FractionalClass import Fractional
 
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
# x3 = x1 + x2
# print(x3)

# x1 = 1.23
# x2 = Fractional(2, 3)

# x3 = x1 + x2
# print(x3)

# x1 = Fractional(2,7)

# x4 = x1 * x2
# print(x4)
# print(x4.to_decimal())

# x5 = x1 - x2
# print(x5)
# print(x5.to_decimal())

# x6 = x1 / x2
# print(x6)
# print(x6.to_decimal())

# x7 = Fractional(2,8)
# print(f"{x1 = }")
# print(f"{x1.to_decimal()}")

# print(f"{x7 = }")
# print(f"{x7.to_decimal()}")

# print({x7.to_decimal()}, {x1.to_decimal()})

# print(x1 == x7)
# print(x1 > x2)
# print(x1 < x2)
# print(x1 >= x7)
# print(x1 <= x7) 