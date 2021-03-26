if __name__ == '__main__':
    returned = [int(el) for el in input().split()]
    rday, rmonth, ryear = returned[0], returned[1], returned[2]

    due = [int(el) for el in input().split()]
    dday, dmonth, dyear = due[0], due[1], due[2]

    if ryear < dyear:
        print(0)

    elif ryear > dyear:
        print(10000)

    else:
        if rmonth < dmonth:
            print(0)

        elif rmonth > dmonth:
            print((rmonth - dmonth) * 500)

        else:
            if rday < dday:
                print(0)

            else:
                print((rday - dday) * 15)
