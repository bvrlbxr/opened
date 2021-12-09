# Задача 3

# Реализуйте класс Student со следующими методами: get_python_skill() -
# получить численную оценку уровня знания Python learn_python() -
# увеличить численную оценку уровня знания Python на 1
#
# Изначально значение численной оценки уровня знания Python - 0.
#
# Пример использования: s = Student() s.get_python_skill()
class Student:

	def __init__(self):
		self.count = 0

	def get_python_skill(self):
		return self.count

	def learn_python(self):
		self.count += 1

# Задача 2

# Реализуйте класс комплексных чисел ComplexNumber, которые можно складывать,
# умножать и сравнивать на равенство с помощью операторов. Пример:
#
# a = ComplexNumber(10, 20) b = ComplexNumber(30, 40) c = ComplexNumber(40, 60)
#
# print(a+b == c)


class ComplexNumber(complex):  # просто наследуем класс лол
	pass

# a = ComplexNumber(10, 20)
# # b = ComplexNumber(30, 40)
# # c = ComplexNumber(40, 60)
# # print(a + b)

class ComplexNumber1:  # используем перегрузку операторов, реализуем свой класс
	def __init__(self, i, j):
		self.rea = i  # действительная часть
		self.im = j  # мнимая часть

	def __add__(self, other):
		return ComplexNumber1(self.rea + other.rea, self.im + other.im)

	def __mul__(self, other):
		return ComplexNumber1(self.rea * other.rea - self.im * other.im, self.rea * other.im + self.im * other.rea)

	def __eq__(self, other):
		if self.rea == other.rea and self.im == other.im:
			return True
		else:
			return False

# a = ComplexNumber1(3,5)
# b = ComplexNumber1(1,4)
# c = ComplexNumber1(4,9)
# print(a+b == c)


# Задача 1
# Реализуйте класс PrimesIterator, позволяющий итерироваться по простым числам,
# начиная с заданного. Примеры использования:
#
# for n in PrimesIterator(42): print(n)
#
# for n in PrimesIterator(): print(n)
from itertools import count
class PrimesIterator:

	def __init__(self, n=2):
		self.start = n

	def __iter__(self):
		return self

	def __next__(self):
		for i in count(self.start):
			prime = True
			for j in range(2, i):
				if i % j == 0:
					prime = False
			if prime:
				self.start = i + 1
				return i

# for i in PrimesIterator():
#      print(i)