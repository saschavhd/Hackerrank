
def cuttingPaperSquares(n, m):
    return (n*m)-1


if __name__ == '__main__':
    nm = [int(el) for el in input().split()]
    n = nm[0]
    m = nm[1]

    print(cuttingPaperSquares(n, m))
