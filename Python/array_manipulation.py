from collections import defaultdict


def arrayManipulation(n, m, queries):
    vals = defaultdict(int)

    for query in queries:
        for i in range(query[0], query[1]+1):
            vals[i] += query[2]

    return max(vals.values())


if __name__ == '__main__':
    nm = [int(el) for el in input().split()]
    n = nm[0]
    m = nm[1]

    queries = []
    for _ in range(m):
        queries.append([int(el) for el in input().split()])

    result = arrayManipulation(n, m, queries)

    print(result)
