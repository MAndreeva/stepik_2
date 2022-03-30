import json
l = []
periodic_table = json.load(open('periodic_table.json', encoding = 'utf-8'))
s = input()
while i < (len(s)-1):
    if s[i] < 'a':
        l.append(s[i] + s[i+1])
    else:
        if s[i] < 'a':
            l.append(s[i])
        else:

        if i+1 == len(s)-1:
            l.append(s[i+1])
res = ''
print (len(l))
for j in range (len(l)):
    res += str( periodic_table[l[j]])

print(res)