if __name__ == '__main__':
    n = int(input())
    arr = [int(el) for el in input().split()]
    arr.reverse()
    res = ""
    for el in arr:
        res += str(el)
        res += " "
    print(res.rstrip())
