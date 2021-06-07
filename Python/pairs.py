

def pairs(k, arr):
    res = 0
    st = set(arr)
    for el in arr:
        if el + k in st:
            res += 1
    return res


if __name__ == '__main__':
    nk = list(map(int, input().split()))
    n, k = nk[0], nk[1]
    arr = list(map(int, input().split()))
    print(pairs(k, arr))
