res = []
with open ("input2.txt") as inf1:
    with open ("input3.txt") as inf2:
        for i in inf1:
            for j in inf2:
                l = j.split()
                s = i[int(l[0]):int(l[1])+1]
                res.append(s)

print (" ".join(res))