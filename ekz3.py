#Задача 1
# def card(cc_number):
#     return '** ' + cc_number[-4:]
# cc_number='1234 5678 9874 5462'
# cc_number=card(cc_number)
# print(card(cc_number))

#Задача 2
# def isPalindrome(s):
#     return s == s[::-1]
#
# s = "lalala"
# ans = isPalindrome(s)
#
# if ans:
#     print("Yes")
# else:
#     print("No")


# Создайте класс Tomato
# 2. Создайте статическое свойство states, которое будет содержать все стадии
# созревания помидора
# 3. Создайте метод __init__(), внутри которого будут определены два динамических
# protected свойства: 1) _index - передается параметром и 2) _state - принимает первое
# значение из словаря states
# 4. Создайте метод grow(), который будет переводить томат на следующую стадию
# созревания
# 5. Создайте метод is_ripe(), который будет проверять, что томат созрел (достиг
# последней стадии созревания
#Задача 3
class Tomato:
    states={1:'green', 2:'yellow', 3:'red'}

    def __init__(self, _index, _state):
        self._index=_index
        self._state=self.states[0]
    def grow(self):
        if self._state!=self.states[2]:
            self._state=self.states[list(self.states.keys())[list(self.states.values()).index(self._state)]+1]
    def is_ripe(self):

        if self._state==self.states[3]:
            return True
        else:
            False


# Создайте класс TomatoBush
# 2. Определите метод __init__(), который будет принимать в качестве параметра
# количество томатов и на его основе будет создавать список объектов класса
# Tomato. Данный список будет храниться внутри динамического свойства tomatoes.
# 3. Создайте метод grow_all(), который будет переводить все объекты из списка
# томатов на следующий этап созревания
# 4. Создайте метод all_are_ripe(), который будет возвращать True, если все томаты из
# списка стали спелыми
# 5. Создайте метод give_away_all(), который будет чистить список томатов после
# сбора урожая


