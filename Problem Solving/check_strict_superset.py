if __name__ == '__main__':
    a = set(input().split())
    n = int(input())
    for _ in range(n):
        if not a.issuperset(set(input().split())):
            print(False)
            break
    else:
        print(True)
