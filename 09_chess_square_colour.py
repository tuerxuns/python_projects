def getChessSquareColor(column, row):
    if (column + row) % 2 == 0 and column < 8 and row < 8:
        return "white"
    elif (column + row) % 2 != 0 and column < 8 and row < 8:
        return "black"
    else:
        return ""


assert getChessSquareColor(0, 0) == "white"

assert getChessSquareColor(1, 0) == "black"

assert getChessSquareColor(0, 1) == "black"

assert getChessSquareColor(7, 7) == "white"

assert getChessSquareColor(0, 8) == ""

assert getChessSquareColor(2, 9) == ""

print("All tests passed!")
