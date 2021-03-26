def resolve_triple(a, b, n):
    first = a
    second = b
    while True:
        current = first + second
        if len(current) >= n:
            return current[n]
        first = second
        second = current


if __name__ == '__main__':
    q = int(input())

    for _ in range(q):
        triple = [el for el in input().split()]
        a = triple[0]
        b = triple[1]
        n = int(triple[2])

        print(resolve_triple(a, b, n))
