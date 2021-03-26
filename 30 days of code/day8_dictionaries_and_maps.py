if __name__ == '__main__':
    dic = {}
    n = int(input())
    for _ in range(n):
        nn = input().split()
        name = nn[0]
        num = int(nn[1])
        dic[name] = num

    while True:
        try:
            q = input()
            if q in dic.keys():
                print("{}={}".format(q, dic[q]))
            else:
                print("Not found")
        except:
            break
