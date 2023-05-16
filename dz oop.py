class Calculytor:

    def __init__(self, a,b):
        self.a=a
        self.b=b


    def s(self):
        print('Сумма', self.a + self.b)

    def s1(self):
        print('Разница',self.a - self.b)

    def s2(self):
        if self.b == 0:
            print("Деление на 0")
        else:
            print('Деление',self.a/self.b)
    def s3(self):
        print('Произведение',self.a * self.b)



cal1=Calculytor(2,1)
cal1.s()
cal1.s1()
cal1.s2()
cal1.s3()



