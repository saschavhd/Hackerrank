def getDivisors(n):
    divisors = []
    for i in range(1, int(n)+1):
        if int(n) % i == 0:
            divisors.append(i)
    return divisors


def bestDivisor(n):
    divs = getDivisors(n)
    largest_digit_sum = float('-inf')
    largest_digit_sum_num = 0
    for el in divs:
        digit_sum = 0
        for char in str(el):
            digit_sum += int(char)
        if digit_sum > largest_digit_sum:
            largest_digit_sum = digit_sum
            largest_digit_sum_num = el
        if digit_sum == largest_digit_sum:
            if el < largest_digit_sum_num:
                largest_digit_sum_num = el
    return largest_digit_sum_num


if __name__ == '__main__':
    n = input()

    print(bestDivisor(n))
