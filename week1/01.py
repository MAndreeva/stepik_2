s = 0
for i in range(1, 1000000003 ):
    if i % 3 == 0 and (i % 10 != 4 or i % 10 != 7):
        s += i
print(s)