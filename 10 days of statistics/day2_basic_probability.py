TOT = 36

res = 0
for i in range(1, 7):
    for ii in range(1, 7):
        if i + ii <= 9:
            res += 1

print(res/TOT)

res = 0
for j in range(1, 7):
    for jj in range(1, 7):
        if j + jj == 6 and j != jj:
            res += 1

print(res/TOT)
