def create(namespace, parent):
    global namespaces
    global variables
    namespaces[namespace] = parent
    variables[namespace] = set()


def add(namespace, var):
    global variables
    variables[namespace].add(var)


def get(namespace, var):
    global x
    while namespace != 'None' and x == '':
        if var in variables[namespace]:
            x = namespace
        else:
            get(namespaces[namespace], var)
    if namespace == 'None':
        x = 'None'


n = int(input())
namespaces = {'global': 'None'}
variables = {'global': set()}
for i in range(n):
    action, namesp, arg = input().split()
    if action == 'create':
        create(namesp, arg)
    elif action == 'add':
        add(namesp, arg)
    elif action == 'get':
        x = ''
        get(namesp, arg)
        print(x)
