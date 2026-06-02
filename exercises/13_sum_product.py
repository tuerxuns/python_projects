def calculateSum(numbers):
    if len(numbers) == 0:
        return 0

    first_number = numbers[0]

    for number in numbers[1:]:
        first_number += number

    return first_number


def calculateProduct(numbers):
    if len(numbers) == 0:
        return 1

    first_number = numbers[0]

    for number in numbers[1:]:
        first_number *= number

    return first_number


assert calculateSum([]) == 0

assert calculateSum([2, 4, 6, 8, 10]) == 30

assert calculateProduct([]) == 1

assert calculateProduct([2, 4, 6, 8, 10]) == 3840

print("All tests passed!")
