if __name__ == '__main__':
    q = int(input())

    for _ in range(q):
        n = int(input())
        a = set(input().split())
        m = int(input())
        b = set(input().split())

        if a.issubset(b):
            print(True)
        else:
            print(False)
