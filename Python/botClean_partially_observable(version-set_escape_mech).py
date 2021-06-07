def get_shortest_dirt(p1, p2, grid):
    '''Get shortest dirt from current bot position'''
    shortest_pos = None
    shortest_distance = float('inf')
    for i in range(n):
        for j in range(n):
            if (grid[i][j] == 'd' and abs(i-p1) + abs(j-p2) < shortest_distance):
                shortest_distance = abs(i-p1) + abs(j-p2)
                shortest_pos = (i, j)
    return shortest_pos


def escape_mech(p1, p2, grid):
    '''
    TL: (0, 0), (0, 1), (1, 0), (2, 1) -> (1, 1)
    TR: (0, 2), (0, 3), (0, 4), (1, 2), (1, 4), (2, 2) -> (1, 3)
    BL: (2, 0), (3, 0), (3, 2), (4, 0), (4, 1) -> (3, 1)
    BR: (2, 3), (2, 4), (3, 4), (4, 2), (4, 3), (4, 4) -> (3, 3)
    '''
    TL = [(0, 0), (0, 1), (1, 0), (2, 1)]
    TR = [(0, 2), (0, 3), (0, 4), (1, 2), (1, 4), (2, 2)]
    BL = [(2, 0), (3, 0), (3, 2), (4, 0), (4, 1)]
    BR = [(2, 3), (2, 4), (3, 4), (4, 2), (4, 3), (4, 4)]
    # Go to must visit spaces
    if (p1, p2) in TL:
        return (1, 1)
    if (p1, p2) in TR:
        return (1, 3)
    if (p1, p2) in BL:
        return (3, 1)
    if (p1, p2) in BR:
        return (3, 3)

    # On must visit spaces
    # TL (1, 1) -> (1, 2)
    # TR (1, 3) -> (2, 3)
    # BL (3, 1) -> (2, 1)
    # BR (3, 3) -> (3, 2)
    if (p1, p2) == (1, 1):
        return (1, 2)
    if (p1, p2) == (1, 3):
        return (2, 3)
    if (p1, p2) == (3, 1):
        return (2, 1)
    if (p1, p2) == (3, 3):
        return (3, 2)


def next_move(p1, p2, grid):
    # Check if bot on dirt
    if grid[p1][p2] == 'd':
        return "CLEAN"

    # Get dirt position
    go_to_pos = get_shortest_dirt(p1, p2, grid)

    # Case no dirt found
    if not go_to_pos:
        go_to_pos = escape_mech(p1, p2, grid)

    # Check correct position output
    pos_dif = (go_to_pos[0]-p1, go_to_pos[1]-p2)
    if pos_dif[1] != 0:
        if pos_dif[1] > 0:
            return "RIGHT"
        else:
            return "LEFT"
    else:
        if pos_dif[0] > 0:
            return "DOWN"
        else:
            return "UP"


if __name__ == "__main__":
    n = 5  # Grid size
    bp = [int(el) for el in input().split()]
    p1 = bp[0]
    p2 = bp[1]

    grid = []
    for _ in range(n):
        temp = []
        for el in input().strip():
            temp.append(el)
        grid.append(temp)

    result = next_move(p1, p2, grid)

    print(result)
