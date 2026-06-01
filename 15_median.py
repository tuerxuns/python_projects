import random


def median(numbers):
    if len(numbers) == 0:
        return None

    elif len(numbers) % 2 != 0:
        sorted_numbers = sorted(numbers)
        median_number_position = len(sorted_numbers) // 2
        return sorted_numbers[median_number_position]

    elif len(numbers) % 2 == 0:
        sorted_numbers = sorted(numbers)
        median_one_position = len(sorted_numbers) // 2 - 1
        median_two_position = len(sorted_numbers) // 2
        average = (
            sorted_numbers[median_one_position] + sorted_numbers[median_two_position]
        ) / 2
        return average


assert median([]) is None

assert median([1, 2, 3]) == 2

assert median([3, 7, 10, 4, 1, 9, 6, 5, 2, 8]) == 5.5

assert median([3, 7, 10, 4, 1, 9, 6, 2, 8]) == 6


random.seed(42)

testData = [3, 7, 10, 4, 1, 9, 6, 2, 8]

for i in range(1000):

    random.shuffle(testData)

    assert median(testData) == 6

print("All tests passed!")
