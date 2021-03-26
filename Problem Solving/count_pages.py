def pageCount(n, p):
    min_pages = 1
    min_pages2 = 1
    if n % 2 == 0:  # only one last page visible
        if p == 1 or p == n:
            return 0
        #front
        for i in range(2, n, 2):
            if i == p or i+1 == p:
                break
            else:
                min_pages += 1
        #back
        for i in range(n-1, 2, -2):
            if i == p or i-1 == p:
                break
            else:
                min_pages2 += 1
        return min(min_pages, min_pages2)
    else:
        min_pages2 = 0
        if p == 1 or p == n or p == n-1:
            return 0
        #front
        for i in range(2, n, 2):
            if i == p or i+1 == p:
                break
            else:
                min_pages += 1
        #back
        for i in range(n, 2, -2):
            # print(i, i-1)
            if i == p or i-1 == p:
                break
            else:
                min_pages2 += 1
        # print(min_pages, min_pages2)

        return min(min_pages, min_pages2)



if __name__ == "__main__":
    n = int(input())
    p = int(input())

    result = pageCount(n, p)

    print(result)
