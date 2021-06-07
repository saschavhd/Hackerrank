from math import ceil

def armySupply(n, m):
    # base = (n//2)*(m//2)
    # if n%2 == 0 and m%2 == 0:
    #     return base
    # if n%2 != 0 and m%2 == 0:
    #     return base + (m//2)
    # if n%2 == 0 and m%2 != 0:
    #     return base + (n//2)
    # else:
    #     return base + ((n//2) + (m//2) + 1)
    return ceil(n/2) * ceil(m/2)


if __name__ == '__main__':
    nm = [int(el) for el in input().split()]
    n = nm[0]
    m = nm[1]

    print(armySupply(n, m))
