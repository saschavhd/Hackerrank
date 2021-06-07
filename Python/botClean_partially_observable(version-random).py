import random

def next_move(p1, p2, grid):
    # Check if bot on dirt
    if grid[p1][p2] == 'd':
        return "CLEAN"

    shortest_pos = None
    # Find shortest dirt
    shortest_distance = float('inf')
    for i in range(n):
        for j in range(n):
            if (grid[i][j] == 'd' and abs(i-p1) + abs(j-p2) < shortest_distance):
                shortest_distance = abs(i-p1) + abs(j-p2)
                shortest_pos = (i, j)

    # Case: can't find dirt
    if not shortest_pos:
        rldu = []
        # Right if
        #   0 <= i <= n-3
        # Left if
        #  2 <= i <= n-1
        # Down if
        # 0 <= j <= n-3
        # Up if
        # 2 <= j <= n-1
        # 1 -> right, 2 -> left, 3 -> down, 4 -> up
        if p2 in range(0, n-1):
            rldu.append(1)
        if p2 in range(2, n):
            rldu.append(2)
        if p1 in range(0, n-1):
            rldu.append(3)
        if p1 in range(2, n):
            rldu.append(4)

        direc = random.choice(rldu)

        if direc == 1:
            return "RIGHT"
        elif direc == 2:
            return "LEFT"
        elif direc == 3:
            return "DOWN"
        elif direc == 4:
            return "UP"

    # Check correct position output
    pos_dif = (shortest_pos[0]-p1, shortest_pos[1]-p2)
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
    n = 5  # grid size
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
