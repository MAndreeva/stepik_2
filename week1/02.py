res = []
with open ("input1.txt") as inf:
    for s in inf:
        l = s.split('    ')
        x = 0
        if l[0] == '+' :
            x= int(l[1])+int(l[2])
        elif l[0] == '-':
            x = int(l[1]) - int(l[2])
        elif l[0] == '*':
            x = int(l[1]) * int(l[2])
        elif l[0] == '//':
            x = int(l[1]) // int(l[2])
        elif l[0] == '**':
            x = int(l[1]) ** int(l[2])
        elif l[0] == '%':
            x = int(l[1]) % int(l[2])
        res.append(str(x))

print (",".join(res))
