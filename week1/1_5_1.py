class MoneyBox:
    def __init__(self, cap=0):
        self.capacity = cap
        self.money=0

    def can_add(self, x):
        if self.money +x <= self.capacity:
            return True
        else:
            return False

    def add(self, x):
        if self.can_add(x) == True:
            self.money +=x
a=MoneyBox(5)
print (a.money, a.capacity)
a.add(1)
print (a.money, a.capacity)
print(a.can_add(5))
a.add(5)
print (a.money, a.capacity)
a.add(4)
print (a.money, a.capacity)


# class MoneyBox:
#     can = True
#     def __init__(self, cap=0):
#         self.capacity = cap
#         self.money=0
#
#     def can_add(self, x):
#         #self.x = 0
#         if self.money +x <= self.capacity:
#             #return True
#             can = True
#         else:
#             can = False
#             #return False
#
#     def add(self, x):
#         #self.x +=1
#         if can_add (self, x) == True:
#             self.money +=x

