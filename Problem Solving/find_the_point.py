def findThePoint(queries):
    res = []
    for el in queries:
        res.append((el[2]+(el[2]-el[0]), el[3]+(el[3]-el[1])))
    return res


if __name__ == '__main__':
    n = int(input())

    queries = []
    for _ in range(n):
        queries.append([int(el) for el in input().split()])

    result = findThePoint(queries)

    for el in result:
        print("{} {}".format(el[0], el[1]))
