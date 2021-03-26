from collections import defaultdict

if __name__ == '__main__':
    K = int(input())
    arr = [int(el) for el in input().split()]

    dic = defaultdict(int)

    for el in arr:
        dic[el] += 1

    for k, v in dic.items():
        if v != K:
            print(k)
