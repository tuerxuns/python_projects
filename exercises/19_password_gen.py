import random


def generatePassword(length):
    lower_case_letters = "abcdefghijklmnopqrstuvwxyz"
    upper_case_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "1234567890"
    special_characters = "~!@#$%^&*()_+"
    all_char = f"{lower_case_letters}{upper_case_letters}{numbers}{special_characters}"

    if length < 12:
        length = 12

    password = []
    # Ensure at least one of each required type
    password.append(random.choice(lower_case_letters))
    password.append(random.choice(upper_case_letters))
    password.append(random.choice(numbers))
    password.append(random.choice(special_characters))

    # Fill the rest
    while len(password) < length:
        password.append(random.choice(all_char))

    # shuffle() modifies the list in-place and returns None
    random.shuffle(password)

    # join() the list into a single string
    return "".join(password)


# Tests
for i in range(10):
    pw = generatePassword(20)
    assert len(pw) == 20
    assert isinstance(pw, str)

print("Generated password example:", generatePassword(16))
print("All tests passed!")
