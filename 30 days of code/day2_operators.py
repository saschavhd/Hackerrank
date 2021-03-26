if __name__ == '__main__':
    cost = float(input())
    tip = int(input())
    tax = int(input())

    print(round(cost + (cost*(tip/100)) + (cost*(tax/100))))
