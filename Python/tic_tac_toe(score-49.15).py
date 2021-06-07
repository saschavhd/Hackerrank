# Axis 0:
# (0, 1), (1, 2), (0, 2)
# Axis 1:
# (0, 1), (1, 2), (0, 2)
#
# _ _ _
# _ _ _
# _ _ _
#
# 0 _ 1
# _ _ _
# 2 _ 3


# Init

n = 3  # Grid size

# Functions

def getReverseGrid(grid):
    '''Gets 0 axis of grid into a reverse array'''
    t = []
    for i in range(n):
        temp = []
        for j in range(n):
            temp.append(grid[j][i])
        t.append(temp)
    return t


def getSpaces(symb, grid):
    '''Returns the positions of a certain symbol (X/O)'''
    t = []
    for i in range(n):
        for j in range(n):
            if grid[i][j] == symb:
                t.append((i, j))
    return t


def getCorners(symb, corners):
    '''Returns array of corners of a certain symbol (X/O)'''
    t = []
    for ind, el in enumerate(corners):
        if el == symb:
            t.append(ind)
    return t


def checkWin(symb, grid, rev_grid, available_spaces):
    '''Returns any winning square, if not found returns false'''
    # Horizontals
    for ind, el in enumerate(grid):
        if el[0] == el[1] and el[0] == symb and (0+ind, 2) in available_spaces:
            return (0+ind, 2)
        elif el[0] == el[2] and el[0] == symb and (0+ind, 1) in available_spaces:
            return (0+ind, 1)
        elif el[1] == el[2] and el[1] == symb and (0+ind, 0) in available_spaces:
            return (0+ind, 0)

    # Verticals
    for ind, el in enumerate(rev_grid):
        if el[0] == el[1] and el[0] == symb and (2, 0+ind) in available_spaces:
            return (2, 0+ind)
        elif el[0] == el[2] and el[0] == symb and (1, 0+ind) in available_spaces:
            return (1, 0+ind)
        elif el[1] == el[2] and el[1] == symb and (0, 0+ind) in available_spaces:
            return (0, 0+ind)

    # Diagonals
    if (
    (grid[0][0] == grid[2][2] and
    grid[0][0] == symb and
    (1, 1) in available_spaces) or
    (grid[0][2] == grid[2][0] and
    grid[0][2] == symb and
    (1, 1) in available_spaces)):
        return (1, 1)

    if (grid[0][0] == grid[1][1] and
    grid[0][0] == symb and
    (2, 2) in available_spaces):
        return (2, 2)

    if (grid[0][2] == grid[1][1] and
    grid[0][2] == symb and
    (2, 0) in available_spaces):
        return(2, 0)

    if (grid[2][0] == grid[1][1] and
    grid[2][0] == symb and
    (0, 2) in available_spaces):
        return(0, 2)

    if (grid[2][2] == grid[1][1] and
    grid[2][2] == symb and
    (0, 0) in available_spaces):
        return(0, 0)

    return False


def centerFilled(grid):
    '''Returns the center square, if not found, returns false'''
    if grid[1][1] == '_':
        return False
    else:
        return grid[1][1]


def nextMove(sym, grid):
    # Check enemy
    if sym == 'X':
        enemy = 'O'
    else:
        enemy = 'X'
    # Init
    default_sym = '_'
    rev_grid = getReverseGrid(grid)  # Grid turned to axis 0
    corners = (grid[0][0], grid[0][2], grid[2][0], grid[2][2])  # Corner vals
    corner_positions = ((0, 0), (0, 2), (2, 0), (2, 2))  # Corners positions
    my_spaces = getSpaces(sym, grid)  # Array of my spaces
    my_corners = getCorners(sym, corners)  # Array of my corners
    enemy_spaces = getSpaces(enemy, grid)  # Array of enemy spaces
    enemy_corners = getCorners(enemy, corners)  # Array of enemy corners
    available_spaces = getSpaces(default_sym, grid)  # Array of available spaces
    available_corners = getCorners(default_sym, corners)  # Arr of av corners
    respos = (0, 0)  # Default result position

    # Check personal winning positions
    check_win = checkWin(sym, grid, rev_grid, available_spaces)
    if check_win:
        return check_win

    # Check enemy winning positions
    check_win = checkWin(enemy, grid, rev_grid, available_spaces)
    if check_win:
        return check_win

    # Check my corners
    # Case -> No corners
    if available_corners:
        if not my_corners:
            return corner_positions[available_corners[0]]

        # Case -> 1 corners
        elif len(my_corners) == 1:
            if my_corners[0] == 0:
                if 3 in available_corners:
                    return corner_positions[3]
            elif my_corners[0] == 1:
                if 2 in available_corners:
                    return corner_positions[2]
            elif my_corners[0] == 2:
                if 1 in available_corners:
                    return corner_positions[1]
            elif my_corners[0] == 3:
                if 0 in available_corners:
                    return corner_positions[0]

        # Case -> 2 corners
        elif len(my_corners) == 2:
            return corner_positions[available_corners[0]]

    # Check center
    if not centerFilled(grid):
        return (1, 1)

    return available_spaces[0]


if __name__ == "__main__":
    sym = input()

    grid = []
    for _ in range(n):
        grid.append(list(input()))

    # print(grid)

    result = nextMove(sym, grid)

    print("{} {}".format(result[0], result[1]))
