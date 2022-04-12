def search(parents_list, parent, child):
    queue = [child]

    while queue:
        current_node = queue.pop()
        if parent in parents_list[current_node] or parent == child:
            return True

        queue.extend(parents_list[current_node])

    return False


class_graph = {}  # dict key - class, value - [parent classes]
n = int(input())
for i in range(n):
    a = [i for i in input().split()]
    if len(a) == 1:
        class_graph[a[0]] = []
    else:
        class_graph[a[0]] = a[2:]


k = int(input())
for i in range(k):
    b = [i for i in input().split()]
    is_parent = search(class_graph, b[0], b[1])
    result = 'Yes' if is_parent else 'No'
    print(result)
