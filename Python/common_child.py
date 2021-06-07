# STRING
# DRING
# "RING"
#-> common elemnts = 4

# STRING
# SRING
# "SRING"
#-> comon elements = 5

from collections import defaultdict


def commonChild(a, b):
    res = 0
    a_list = list(a)
    b_list = list(b)
    a_set = set(a)
    b_set = set(b)

    # print(a_set, b_set)
    # print(a_set.difference(b_set))

    for el in a_set.difference(b_set):
        while el in a_list:
            a_list.remove(el)

    for el in b_set.difference(a_set):
        while el in b_list:
            b_list.remove(el)

    print(a_list)
    print(b_list)

    return res


if __name__ == "__main__":
    a_string = input()
    b_string = input()

    result = commonChild(a_string, b_string)
    print(result)
