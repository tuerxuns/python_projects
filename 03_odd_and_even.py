def isOdd(number):
    if number % 2 == 1:
        return True
    else:
        return False


def isEven(number):
    if number % 2 == 0:
        return True
    else:
        return False


assert not isOdd(42)

assert isOdd(9999)

assert not isOdd(-10)

assert isOdd(-11)

assert not isOdd(3.1415)

assert isEven(42)

assert not isEven(9999)

assert isEven(-10)

assert not isEven(-11)

assert not isEven(3.1415)

print("All tests passed!")
