from bisect import bisect

def triplets(a, b, c):
    a, b, c = sorted(set(a)), set(b), sorted(set(c))
    return sum((bisect(a, x) * bisect(c, x) for x in b))


if __name__ == '__main__':
    lens = list(map(int, input().split()))

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    print(triplets(a, b, c))
