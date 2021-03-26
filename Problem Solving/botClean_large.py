def next_move(n, m, p1, p2, grid):
    # Check if bot on dirt
    if grid[p1][p2] == 'd':
        return "CLEAN"

    # Find shortest dirt
    shortest_distance = float('inf')
    for i in range(n):
        for j in range(m):
            if (grid[i][j] == 'd' and abs(i-p1) + abs(j-p2) < shortest_distance):
                shortest_distance = abs(i-p1) + abs(j-p2)
                shortest_pos = (i, j)

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
    bp = [int(el) for el in input().split()]
    nm = [int(el) for el in input().split()]
    p1 = bp[0]
    p2 = bp[1]
    n = nm[0]
    m = nm[1]

    grid = []
    for _ in range(n):
        temp = []
        for el in input().strip():
            temp.append(el)
        grid.append(temp)

    result = next_move(n, m, p1, p2, grid)

    print(result)
