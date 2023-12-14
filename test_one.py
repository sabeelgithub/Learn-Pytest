import math
def test_sqt():
    num1 = 25
    assert math.sqrt(num1) == 5

    num2 = 6
    assert math.sqrt(num2) != 1

    assert math.ceil(1.5) == 2
    assert math.floor(1.5) == 1

def testsquare():
   num = 7
   assert 7*7 != 40

def tesequality():  # this not treating as test function
   assert 10 == 11

