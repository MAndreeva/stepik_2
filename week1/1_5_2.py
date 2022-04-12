class Buffer:
    def __init__(self):
        self.count = 0
        self.content = []
        self.summ = 0

    def add(self, *a):
        for i in range(len(a)):
            self.content.append(a[i])
            self.count += 1
            self.summ += a[i]
            if self.count >= 5:
                print(self.summ)
                self.count = 0
                self.summ = 0
                self.content = []

    def get_current_part(self):
        return self.content


buf = Buffer()
buf.add(1, 2, 3)
buf.get_current_part()  # вернуть [1, 2, 3]
buf.add(4, 5, 6)  # print(15) – вывод суммы первой пятерки элементов
buf.get_current_part()  # вернуть [6]
buf.add(7, 8, 9, 10)  # print(40) – вывод суммы второй пятерки элементов
buf.get_current_part()  # вернуть []
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)  # print(5), print(5) – вывод сумм третьей и четвертой пятерки
buf.get_current_part()  # вернуть [1]
