import importlib

leap_year_mod = importlib.import_module("20_leap_year")


def isValidDate(year, month, day):
    if month in (4, 6, 9, 11):
        return day in range(1, 31)
    elif month == 2:
        if leap_year_mod.isLeapYear(year):
            return day in range(1, 30)
        return day in range(1, 29)
    elif month in (1, 3, 5, 7, 8, 10, 12):
        return day in range(1, 32)
    return False


assert isValidDate(1999, 12, 31) == True

assert isValidDate(2000, 2, 29) == True

assert isValidDate(2001, 2, 29) == False

assert isValidDate(2029, 13, 1) == False

assert isValidDate(1000000, 1, 1) == True

assert isValidDate(2015, 4, 31) == False

assert isValidDate(1970, 5, 99) == False

assert isValidDate(1981, 0, 3) == False

assert isValidDate(1666, 4, 0) == False
