from math import ceil

def minHeightTriangle(a, b):
    # Area(triangle) = (base*height)/2
    # -> height = Area*2/base
    return ceil((a*2)/b)


if __name__ == '__main__':
    b, a = [int(el) for el in input().split()]

    print(minHeightTriangle(a, b))
