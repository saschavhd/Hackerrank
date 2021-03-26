import re

if __name__ == '__main__':
    t = int(input())

    arr = []
    for _ in range(t):
        name_email = [el for el in input().split()]
        name = name_email[0]
        email = name_email[1]

        if re.search('[a-z]{1,}@gmail.[a-z]{1,}', email):
            arr.append(name)

    arr.sort()
    for el in arr:
        print(el)
