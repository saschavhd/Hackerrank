# def amount_ones(a):
#     largest = 1
#     i = 0
#     while i < len(a):
#         consec = 1
#         while (
#             i < len(a) - 1 and
#             a[i] == '1' and
#             a[i+1] == a[i]
#         ):
#             if i == len(a) - 2 and a[i+1] == a[i]:
#                 consec += 1
#                 break
#             i += 1
#             consec += 1
#
#
#         if consec > largest:
#             largest = consec
#         i += 1
#     return largest
#
#
# if __name__ == '__main__':
#     print(amount_ones(bin(int(input()))[2:]))

if __name__ == '__main__':
    # print(max([len(x) for x in bin(int(input()))[2:].split('0')]))
    print(max(map(lambda x: len(x), bin(int(input()))[2:].split('0'))))
