def movingTiles(t):
    if V1 > V2:
        return (((V1*t + (L/(2**(1/2))))-(V2*t - (L/(2**(1/2)))))**2)/2
    else:
        return (((V2*t + (L/(2**(1/2))))-(V1*t - (L/(2**(1/2)))))**2)/2


if __name__ == '__main__':
    LV = [int(el) for el in input().split()]
    L = LV[0]
    V1 = LV[1]
    V2 = LV[2]

    q = int(input())
    for _ in range(q):
        print(movingTiles(int(input())))
