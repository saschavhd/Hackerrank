if __name__ == '__main__':
    nm = [int(el) for el in input().split()]

    test = [int(el) for el in input().split()]
    a = set([int(el) for el in input().split()])
    b = set([int(el) for el in input().split()])

    hap = sum([(el in a) - (el in b) for el in test])

    print(hap)
