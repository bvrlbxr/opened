# Задача 6
# Веб-сайт требует, чтобы пользователи вводили пароль для регистрации, соответствующий определенным требованиям. Напишите программу для проверки правильности ввода пароля пользователями.
# Ниже приведены критерии проверки пароля:
# 1. Минимум 1 буква латинского алфавита в нижнем регистре [az]
# 2. Минимум 1 число от [0–9]
# 3. Минимум 1 буква латинского алфавита в верхнем регистре [AZ]
# 4. Минимум 1 специальный символ
# 5. Минимальная длина пароля : 6
# 6. Максимальная длина пароля: 12
# Программа должна возвращать True или False.
# Формат ввода
#
# Passw1#0rd
# Формат вывода
#
# True

def passchck(arg):
	alphabet = 'abcdefghijklmnopqrstuvwxyz'
	digmem = False
	uppermem = False
	lowmem = False
	symmem = False
	alpmem = False

	if 6 <= len(arg) <= 12:
		for i in str(arg):
			if i in alphabet:
				alpmem = True
			if i.isdigit():
				digmem = True
			if not i.isalpha() and not i.isdigit():
				symmem = True
			if i.isupper():
				uppermem = True
			if i.lower():
				lowmem = True
	return digmem and uppermem and lowmem and symmem and alpmem


# Задача 2

# Напишите функцию, которая будет возвращать самое длинное слово в предложении.
# Если найдено более одного слова, то функция возвращает первое.
# Формат ввода

# The Tower of London was built in the 15th century
# Формат вывода
#
# century
def longestword(args):
	args = args + ' '
	lnght = 0
	lnght_new = 0
	word_max = ''
	word = ''

	for i in args:
		if i != ' ' and i != args[len(args) - 1]:
			word = word + i
			lnght = lnght + 1
		else:
			if lnght > lnght_new:
				lnght_new = lnght
				word_max = word

			elif lnght == lnght_new:
				word_max = word_max

			lnght = 0
			word = ''
	return word_max


# # Задача 1
# Создайте функцию, которая принимает переменное количество аргументов
# и находит среднее арифметическое ненулевых из них.
# Обратите внимание на формат вывода
# 1 2 3        --->   2
# 2 0 0 2 2    --->   2
# 2 0 2 1 1    --->   1.5

# Формат ввода
# 1 2 3 0 0
# Формат вывода
# 2
def mid_ar(args):
	summ = 0
	count = 0
	res = 0
	for i in args.split():
		if not i.isalpha() and float(i) != 0.0:
			summ = summ + float(i)
			count += 1
	if count != 0:
		res = summ / count

	if res - int(res) == 0:
		res = int(res)
	else:
		res = res

	return res

# Задача 3
# Напишите функцию, которая возвращает самую длинную неповторяющуюся подстроку для входной строки.
# Если несколько подстрок совпадают по длине, функция возвращает ту, которая встречается первой.
# xxxxx     ->   x
# abcdefa   ->   abcdef

# Формат ввода
# abcabcbb
# Формат вывода
# abc
def substr(s):

	sub = ''
	sub1 = ''

	for i in s:

		if i not in sub:
			sub += i
		elif i not in sub1:
			sub1 = sub
			sub = i

		if len(sub) > len(sub1):
			a = sub
		if len(sub) == len(sub1):
			a = sub1

	return a

# Задача 4
# Строка считается действительной, если все символы в строке встречаются одинаковое количество раз.
# Также допустимо, если для выполнения этого условия будет достаточно удалить 1 символ из строки.
# Напишите функцию, которая возвращает True, если строка действительна и False, если нет.
#
# abc    ->  True
# abcc   ->  True

# Формат ввода
# abccc
# Формат вывода
# False

def str_validity(s):
	sub = ''
	counter1 = 0
	counter2 = 0
	flag = False

	for i in s:
		if i not in sub:
			sub += i
			counter1 = s.count(i)

		if counter1 != counter2 and not flag:
			counter2 = counter1
			flag = True

		if counter1 == counter2 and flag:
			a = True
		if i == s[-1:] and (counter1 - 1 == counter2) and flag:
			a = True
		elif counter1 != counter2 and flag:
			a = False
			break

	return a

# Задача 5
# Создайте функцию, которая принимает на вход римское число как строку и преобразует ее в целое число,
# возвращая результат.
# Функция должна работать для всех римских цифр, представляющих натуральные числа меньше 4000.

# Формат ввода
# MMMCMV
# Формат вывода
# 3905

def roma(s):

	count = 0
	summ = 0
	count1 = 0
	voc1 = {'I': 1, 'X': 10, 'C': 100, 'M': 1000, 'V': 5, 'L': 50, 'D': 500}

	for i, j in enumerate(s):
		count += 1

		if i != len(s) - 1 and j != s[0]:
			if j == 'V' and s[i - 1] == 'I':
				summ += 4
				count1 = count
			elif j == 'L' and s[i - 1] == 'X':
				summ += 40
				count1 = count
			elif j == 'D' and s[i - 1] == 'C':
				summ += 400
				count1 = count
			elif j == 'I' and s[i + 1] == 'X':
				summ += 9
				count1 = count
			elif j == 'X' and s[i + 1] == 'C':
				summ += 90
				count1 = count
			elif j == 'C' and s[i + 1] == 'M':
				summ += 900
				count1 = count

		if j in s and (count - 1 > count1 or count == 1):
				summ += voc1[j]
				count1 = 0
	return summ

# Задача 7
# На вход в программу поступает цвет CSS RGB(A), необходимо определить действителен ли его формат.
# Создайте функцию, которая принимает строку (например, «rgb (0, 0, 0)») и возвращает True, если формат правильный,
# в противном случае возвращает False. Данные могут поступать как в формате rgb, так и rgba.

# Допустимые значения:
# rgb(0 - 255, 0 - 255, 0 - 255), rgb(0 - 100 %, 0 - 100 %, 0 - 100 %), rgba(0 - 255, 0 - 255, 0 - 255, 0 - 1)
# Возможные  форматы ввода:

# rgb(0 %, 50 %, 100 %) - --> True
# rgba(0, 0, 0, 0) - --> True
# rgb(255, 255, 255) - --> True
# rgb(0,, 0)        ---> False
# rgb(-1, 0, 0) - --> False
# rgba(0, 0, 0, 1.5) - --> False
# rgba(0, 0, 0, 0.5) - --> True

# Формат ввода
# rgb(-1,0,0)

# Формат вывода
# False
def color_re(s):
	type = ''
	codes = []
	result = False
	number = ''
	for i in s[:4]:
		if i.isalpha():
			type += i

	for i in s:
		if i.isdigit() or i == '.':
			number += i
		if (i == ',' or i == ')') and number != '':
			codes.append(number)
			number = ''

	if type == 'rgba' and len(codes) == 4 and '-' not in s and '%' not in s:
		if 0 <= float(codes[3]) <= 1:
			for i in codes[2]:
				if 0 <= int(i) <= 255:
					result = True
				else:
					result = False
		else:
			result = False

	elif type == 'rgb' and len(codes) == 3:
		if '%' in s and '-' not in s:
			if s.count('%') == 3:
				for i in codes:
					if 0 <= int(i) <= 100:
						result = True
					else:
						result = False
		elif '%' not in s and '-' not in s:
			for i in codes:
				if 0 <= int(i) <= 255:
					result = True
				else:
					result = False
	return result


# print(color_re('rgb(0%,50%,100%)'))
# print(color_re('rgba(0,0,0,0)'))
# print(color_re('rgb(255,255,255)'))
# print(color_re('rgb(0,,0)'))
# print(color_re('rgb(-1,0,0)'))
# print(color_re('rgba(0,0,0,1.5)'))
# print(color_re('rgba(0,0,0,0.5)'))
def func(a, b, c, d):

	return 0


func (1, 2, 3, 4)