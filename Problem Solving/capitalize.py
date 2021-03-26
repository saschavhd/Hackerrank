def solve(s):
    newstring = ''
    for ind, char in enumerate(s):
        if ind == 0 and char.isalpha():
            newstring += char.upper()
        elif s[ind-1] == ' ' and char.isalpha() and ind > 0:
            newstring += char.upper()
        else:
            newstring += char
    return newstring


if __name__ == '__main__':
    print(solve(input()))
