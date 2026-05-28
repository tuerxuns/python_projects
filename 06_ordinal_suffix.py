def ordinalSuffix(number):
    string_number = str(number)
    last_number = string_number[-1]
    if len(string_number) >= 2 and string_number[-2] == "1":
        return f"{number}th"
    if last_number == "1":
        return f"{number}st"
    elif last_number == "2":
        return f"{number}nd"
    elif last_number == "3":
        return f"{number}rd"
    else:
        return f"{number}th"


assert ordinalSuffix(0) == "0th"

assert ordinalSuffix(1) == "1st"

assert ordinalSuffix(2) == "2nd"

assert ordinalSuffix(3) == "3rd"

assert ordinalSuffix(4) == "4th"

assert ordinalSuffix(10) == "10th"

assert ordinalSuffix(11) == "11th"

assert ordinalSuffix(12) == "12th"

assert ordinalSuffix(13) == "13th"

assert ordinalSuffix(14) == "14th"

assert ordinalSuffix(101) == "101st"


print("All tests passed!")
