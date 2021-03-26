import math

def weightedMean(X, W):
    num = 0
    den = sum(W)
    for i in range(len(X)):
        num += (X[i] * W[i])
    return round(num/den, 1)


if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    weights = list(map(int, input().rstrip().split()))

    print(weightedMean(vals, weights))
