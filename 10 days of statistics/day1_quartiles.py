import math
from statistics import median

def quartiles(arr):
    arr.sort()
    N = len(arr)
    if N % 2 == 0:
        return list(map(int, [median(arr[:math.floor(N/2)]), median(arr), median(arr[math.floor(N/2):])]))
    else:
        return list(map(int, [median(arr[:math.floor(N/2)]), median(arr), median(arr[math.floor(N/2)+1:])]))


if __name__ == '__main__':
    n = int(input())
    print(quartiles([int(el) for el in input().split()]))
