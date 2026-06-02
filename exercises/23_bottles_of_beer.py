def beer_song():
    beer = 99
    while beer >= 2:
        if beer > 2:
            print(
                f"{beer} bottles of beer on the wall,\n{beer} bottles of beer,\nTake one down,\nPass it around,\n{beer - 1} bottles of beer on the wall,"
            )
        else:
            print(
                f"{beer} bottles of beer on the wall,\n{beer} bottles of beer,\nTake one down,\nPass it around,\n{beer - 1} bottle of beer on the wall,"
            )
        beer -= 1
    print(
        "1 bottle of beer on the wall,\n1 bottle of beer,\nTake one down,\nPass it around,"
    )
    print("No more bottles of beer on the wall!")


beer_song()
