def checkio(game_result):
    count = {'X': [[0, 0, 0], [0, 0, 0], [0, 0]], 'O': [[0, 0, 0], [0, 0, 0], [0, 0]]}
    
    rows = len(game_result)
    
    for row in range(rows):
        for col in range(len(game_result[row])):
            player = game_result[row][col]
            print player + " " + str(row) + " " + str(col)
            if player != '.':
                count[player][0][row] += 1
                count[player][1][col] += 1
                if row == col:
                    count[player][2][0] += 1
                if row + col == rows - 1:
                    count[player][2][1] += 1

                if count[player][0][row] == 3 or count[player][1][col] == 3 or count[player][2][0] == 3 or count[player][2][1] == 3:
                    return player

    print(count)
    return "D"

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
