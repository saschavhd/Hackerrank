def is_prime(n):
    if n <= 3:
        if n > 1:
            return 'Prime'
        else:
            return 'Not prime'

    elif n % 2 == 0 or n % 3 == 0:
        return 'Not prime'

    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return 'Not prime'

        i += 6

    return 'Prime'


if __name__ == '__main__':
    t = int(input())

    for _ in range(t):

        n = int(input())

        print(is_prime(n))
