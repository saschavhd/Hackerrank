def bubbleSort(arr):
    total_swaps = 0
    for i in range(len(arr)):
        swaps = 0

        for j in range(n-1):
            if (arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swaps += 1

        total_swaps += swaps

        if swaps == 0:
            print("Array is sorted in {} swaps.".format(total_swaps))
            print("First Element: {}".format(arr[0]))
            print("Last Element: {}".format(arr[-1]))
            break


if __name__ == '__main__':
    n = int(input())

    arr = [int(el) for el in input().split()]

    bubbleSort(arr)
