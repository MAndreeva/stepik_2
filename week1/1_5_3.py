class A:
    val = 1

    def foo(self):
        A.val += 2

    def bar(self):
        self.val += 1

        self.__class__.val


a = A()
b = A()

a.bar() # 1
a.foo() # 3

c = A()