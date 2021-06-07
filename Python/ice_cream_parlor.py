from collections import OrderedDict

def getIcePair(m, n, ice):
    table = {}
    for ind, el in enumerate(ice):
        table[ind+1] = el
    dic = orderedDict(sorted(d.items()))

    for k, v in dic:
        l, r = 0, len(ice) - 1
        while l <= r:
            mid = l + (r-l)//2

            if ice[mid] == (m - el):
                print(":{}{}".format(el, ice[mid]))
                return sorted([ind+1, mid+1])

            elif m - el < array[mid]:
                r = mid - 1

            else:
                l = mid + 1


if __name__ == "__main__":
    q = int(input())

    for _ in range(q):

        m = int(input())

        n = int(input())

        ice = [int(el) for el in input().split()]

        result = getIcePair(m, n, ice)

        print(result[0], result[1])
