def stdDev(arr):
    N = len(arr)
    avg = sum(arr)/N
    nom = 0
    for i in range(N):
        nom += ((arr[i]-avg) ** 2)
    return float(round((nom/N) ** (1/2), 1))


if __name__ == '__main__':
    n = int(input())

    print(stdDev([int(el) for el in input().split()]))
