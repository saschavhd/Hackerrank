def get256thday(year):
    if year < 1918:
        if year % 4 == 0:
            return "12.09.{}".format(year)
        else:
            return "13.09.{}".format(year)
    else:
        # if year == 1918:
        #     return "31.08.{}".format(year)
        if year % 400 == 0:
            return "12.09.{}".format(year)
        if year % 100 == 0:
            return "13.09.{}".format(year)
        if year % 4 == 0:
            return "12.09.{}".format(year)
        else:
            return "13.09.{}".format(year)


if __name__ == "__main__":
    year = int(input())

    result = get256thday(year)
    print(result)
