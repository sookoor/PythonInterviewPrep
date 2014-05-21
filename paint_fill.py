def _paint_fill(screen, x, y, color, new_color):
    if x >= 0 and x < len(screen) and y >= 0 and y < len(screen[0]) and screen[x][y] == color:
        screen[x][y] = new_color
        _paint_fill(screen, x - 1, y, color, new_color)
        _paint_fill(screen, x + 1, y, color, new_color)
        _paint_fill(screen, x, y - 1, color, new_color)
        _paint_fill(screen, x, y + 1, color, new_color)

def paint_fill(screen, x, y, new_color):
    _paint_fill(screen, x, y, screen[x][y], new_color)

if __name__ == "__main__":
    screen = [[0, 0, 0, 0],
              [0, 1, 1, 0],
              [0, 1, 1, 0],
              [0, 0, 0, 0]]

    paint_fill(screen, 0, 0, 2)
    print screen
