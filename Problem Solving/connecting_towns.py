# Init

M = 1234567  # Modulo

# Functions

def connectingTowns(routes):
    res = 1
    for el in routes:
        # res = (res *(el % M)) % M
        # This option should be more efficient because of operations in place
        res *= (el % M)
        res %= M

    return res



if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n = int(input())
        routes = [int(el) for el in input().split()]

        print(connectingTowns(routes))
