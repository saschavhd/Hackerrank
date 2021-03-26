def is_weird(n):
    if n % 2 != 0:
        return "Weird"
    elif n in range(2, 6):
        return "Not Weird"
    elif n in range(6, 21):
        return "Weird"
    else:
        return "Not Weird"


if __name__ == '__main__':
    n = int(input())

    print(is_weird(n))
