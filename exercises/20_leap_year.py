def isLeapYear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    else:
        return False


if __name__ == "__main__":
    assert not isLeapYear(1999)
    assert isLeapYear(2000)
    assert not isLeapYear(2001)
    assert isLeapYear(2004)
    assert not isLeapYear(2100)
    assert isLeapYear(2400)
    print("All tests passed!")
