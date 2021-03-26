def handshake(k):
    return sum(range(k))


if __name__ == '__main__':
    n = int(input())

    for _ in range(n):
        print(handshake(int(input())))
