z = []
x = [1]
y = z
q = x
w = [3]

objects = [z, x, y, q, w]
s = set()
for i in range(len(objects)):
    s.add(id(objects[i]))
print(len(s))