class ExtendedStack(list):
   # def __init__(self):

    def sum(self):
        a = self.pop()
        b = self.pop()
        self.append(a+b)

    def sub(self):
        a = self.pop()
        b = self.pop()
        self.append(a - b)

    def mul(self):
        self.append(self.pop()*self.pop())
        #a = self.pop()
        #b = self.pop()
        #self.append(a * b)

    def div(self):
        a = self.pop()
        b = self.pop()
        self.append(a // b)

ex_stack = ExtendedStack([1, 2, 3, 4, -3, 3, 5, 10])
ex_stack.div()
print(ex_stack[-1])
#assert ex_stack.pop() == 2
ex_stack.sub()
print(ex_stack[-1])
#assert ex_stack.pop() == 6
ex_stack.sum()
print(ex_stack[-1])
#assert ex_stack.pop() == 7
ex_stack.mul()
print(ex_stack[-1])
print(len(ex_stack))
#assert ex_stack.pop() == 2
#assert len(ex_stack) == 0