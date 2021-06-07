def maxDraws(k):
    return k+1


if __name__ == '__main__':
    n = int(input())

    for _ in range(n):
        print(maxDraws(int(input())))
