def countApplesAndOranges(s, t, a, b, apples, oranges):
    apoh = 0
    aroh = 0
    for el in apples:
        apple_pos = el + a
        if apple_pos in range(s, t+1):
            apoh += 1

    for el in oranges:
        orange_pos = el + b
        if orange_pos in range(s, t+1):
            aroh += 1

    print(apoh)
    print(aroh)


if __name__ == "__main__":
    s, t = [int(el) for el in input().split()]
    a, b = [int(el) for el in input().split()]
    m, n = [int(el) for el in input().split()]
    apples = [int(el) for el in input().split()]
    oranges = [int(el) for el in input().split()]

    countApplesAndOranges(s, t, a, b, apples, oranges)
