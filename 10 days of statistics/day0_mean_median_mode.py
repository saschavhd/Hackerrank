import math
from collections import defaultdict

def getMean(arr):
    if len(arr) % 2 != 0:
        return arr[math.floor(len(arr)/2)]
    else:
        return (arr[len(arr)//2] + arr[(len(arr)//2)-1])/2


def getAvg(arr):
    return sum(arr)/len(arr)


def getMode(arr):
    dic = defaultdict(int)
    for el in arr:
        dic[el] += 1
    mx = max(dic.values())
    mi = float('inf')
    for k, v in dic.items():
        if v == mx and k < mi:
            mi = k
    return mi


if __name__ == '__main__':
    n = int(input())
    a = [int(el) for el in input().split()]
    a.sort()
    print(getAvg(a))
    print(getMean(a))
    print(getMode(a))
