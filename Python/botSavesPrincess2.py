def nextMove(n, r, c, grid):
    player_pos = (r, c)
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'p':
                princess_pos = (i, j)
                break
    pos_dif = (princess_pos[0]-player_pos[0], princess_pos[1]-player_pos[0])
    if pos_dif[0] != 0:
        if pos_dif[0] > 0:
            return "DOWN"
        else:
            return "UP"
    else:
        if pos_dif[1] > 0:
            return "RIGHT"
        else:
            return "LEFT"


if __name__ == "__main__":
    n = int(input())
    pp = [int(el) for el in input().split()]
    p1 = pp[0]
    p2 = pp[1]

    grid = []
    for _ in range(n):
        grid.append(input().strip())

    result = nextMove(n, p1, p2, grid)

    print(result)
