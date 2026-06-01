import random


def rollDice(numberofDice):
    if numberofDice == 0:
        return 0
    initial_dice = 0
    for dice in range(numberofDice):
        dice = random.randint(1, 6)
        initial_dice += dice
    return initial_dice


assert rollDice(0) == 0

assert rollDice(1000) != rollDice(1000)

for i in range(1000):

    assert 1 <= rollDice(1) <= 6

    assert 2 <= rollDice(2) <= 12

    assert 3 <= rollDice(3) <= 18

    assert 100 <= rollDice(100) <= 600

print("All tests passed!")
