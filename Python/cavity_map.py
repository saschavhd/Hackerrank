def cavityMap(n, grid):
    cavities = []
    for i in range(1, n-1):
        for j in range(1, n-1):
            if (grid[i][j] > grid[i-1][j] and
                grid[i][j] > grid[i][j-1] and
                grid[i][j] > grid[i][j+1] and
                grid[i][j] > grid[i+1][j]):
                cavities.append((i, j))
    for el in cavities:
        i, j = el
        grid[i][j] = 'X'
    return grid


if __name__ == '__main__':
    n = int(input())
    grid = []
    for _ in range(n):
        temp = []
        for c in input():
            temp.append(c)
        grid.append(temp)

    result = cavityMap(n, grid)
    print('-'*100)
    for el in result:
        for y in el:
            print(y, end='')
        print()
