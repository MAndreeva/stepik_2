def get(parent, child):
    # global x
    if parent not in class_graph or child not in class_graph :
        return 'No'
    if parent in class_graph[child] or parent == child:
        # x = 'Yes'
        return 'Yes'
    # for i in range(len(class_graph[child])):
    for i in class_graph[child]:
        # while class_graph[child] != 'None' and x == '':
        if class_graph[child] != []:  # and x == '':   if not
            val = get(parent, i)
            if val == 'Yes':
                return 'Yes'
            # get(parent, class_graph[child][i])
    return 'No'
    # return 'No'


class_graph = {}  # dict key - class, value - [parent classes]
n = int(input())
for i in range(n):
    a = [i for i in input().split()]
    if len(a) == 1:
        class_graph[a[0]] = []
    else:
        for k in range(2, len(a)):
            if k == 2:
                class_graph[a[0]] = [a[k]]
            else:
                class_graph[a[0]].append(a[k])
print(class_graph)
k = int(input())
for i in range(k):
    b = [i for i in input().split()]
    # x = ''
    # get(b[0], b[1])
    # if x == '':
    # x = 'No'
    print(get(b[0], b[1]))
