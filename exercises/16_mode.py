import random


def mode(numbers):
    if len(numbers) == 0:
        return None

    number_count = {}

    most_common_number = None
    most_common_number_count = 0

    for number in numbers:
        if number not in number_count:
            number_count[number] = 0
        number_count[number] += 1

        if number_count[number] > most_common_number_count:
            most_common_number = number
            most_common_number_count = number_count[number]

    return most_common_number


assert mode([]) is None

assert mode([1, 2, 3, 4, 4]) == 4

assert mode([1, 1, 2, 3, 4]) == 1


random.seed(42)

testData = [1, 2, 3, 4, 4]

for i in range(1000):

    random.shuffle(testData)

    assert mode(testData) == 4

print("All tests passed!")
