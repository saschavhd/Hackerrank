from math import floor

def displayPathToPrincess(n, grid):
    # Initialise
    player_pos = (floor(n/2), floor(n/2))
    res = []

    # Get princess position
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'p':
                princess_pos = (i, j)
                break

    # Get difference and calculate moves from it
    pos_dif = (princess_pos[0]-player_pos[0], princess_pos[1]-player_pos[1])

    if pos_dif[0] > 0:
        for _ in range(abs(pos_dif[0])):
            res.append("DOWN")
    else:
        for _ in range(abs(pos_dif[0])):
            res.append("UP")

    if pos_dif[1] > 0:
        for _ in range(abs(pos_dif[0])):
            res.append("RIGHT")
    else:
        for _ in range(abs(pos_dif[1])):
            res.append("LEFT")
    return res


if __name__ == "__main__":
    n = int(input())

    grid = []
    for _ in range(n):
        grid.append(input().strip())

    result = displayPathToPrincess(n, grid)

    for el in result:
        print(el)
