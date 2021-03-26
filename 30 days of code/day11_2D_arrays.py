# Always 6x6 grid, so iterate over the inner 4x4 and get sum of (i,j) (i-1, j-1)
# (i-1, j), (i-1, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)

def hourglass(arr):
    maxSum = float('-inf')
    for i in range(1, 5):
        for j in range(1, 5):
            sum = arr[i][j] + arr[i-1][j-1] + arr[i-1][j] + arr[i-1][j+1] + arr[i+1][j-1] + arr[i+1][j] + arr[i+1][j+1]
            if sum > maxSum:
                maxSum = sum
    return maxSum

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append([int(el) for el in input().split()])

    print(hourglass(arr))
