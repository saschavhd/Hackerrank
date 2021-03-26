def dexing_strings(string):
    res = ""
    for i in range(0, len(string), 2):
        res += string[i]
    res += " "
    for j in range(1, len(string), 2):
        res += string[j]
    return res


if __name__ == '__main__':
    q = int(input())

    for _ in range(q):
        print(dexing_strings(input()))
