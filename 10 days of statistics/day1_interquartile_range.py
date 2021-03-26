import math
from statistics import median

def quartiles(arr):
    arr.sort()
    N = len(arr)
    if N % 2 == 0:
        return list(map(int, [median(arr[:math.floor(N/2)]), median(arr), median(arr[math.floor(N/2):])]))
    else:
        return list(map(int, [median(arr[:math.floor(N/2)]), median(arr), median(arr[math.floor(N/2)+1:])]))


def expandSet(val, freq):
    res = []
    for i in range(len(val)):
        res.extend([val[i]]*freq[i])
    return sorted(res)


def interQuartile(val, freq):
    real_set = expandSet(val, freq)
    return float(round(quartiles(real_set)[-1] - quartiles(real_set)[0], 1))

if __name__ == '__main__':
    n = int(input())

    val = [int(el) for el in input().split()]
    freq = [int(el) for el in input().split()]

    print(interQuartile(val, freq))
