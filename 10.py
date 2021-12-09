# Задача 1
# Дан файл "titanic.csv" в формате .csv, который можно открыть командой pd.read_csv("titanic.csv")
#
# Каждая строка набора данных - это отдельный человек, который либо выжил, либо не выжил (столбец "Survived").
#
# В данной задаче необходимо определить количество людей в наборе данных возраст которых строго больше N.
# Где N - некое целое число от 0 до 100, которое подается на вход вашей функции.
# На выходе ожидается также целое число - количество пассажиров Титаника.


# import pandas as pd
#
# people = pd.read_csv("titanic.csv")
# count = 0
# age_set = int(input())
#
# if 0 < age_set < 100:
# 	for i in people['Age']:
# 		try:
# 			if int(i) > age_set:
# 				count += 1
# 		except: count = count
#
# 	print(count)


# Задача 2
# Дан файл "titanic.csv" в формате .csv, который можно открыть командой pd.read_csv("titanic.csv")
# Каждая строка набора данных - это отдельный человек, который либо выжил, либо не выжил (столбец "Survived").
# В данной задаче необходимо определить один из статистических показателей: количество,
# максимум, минимум - по указанной группе пассажиров, по указанному признаку.
# Например, найти количество представителей выживших/не выживших пассажиров ("Survived") по столбцу "Pclass".
# На вход получаем: столбец по которому группируем, столбец для которого ищем статистику,
# название самой статистики (count, min, max)
# На выходе печатаем столько строк, сколько получилось после группировки по указанному столбцу.
# В каждой строке сначала название группы (уникальное значение столбца, по которому группировали),
# затем пробел, затем значение статистики для указанной группы.

# import pandas as pd
#
# people = pd.read_csv("titanic.csv")
# s = input().split()
#
# if s[2] == 'count':
# 	i = people.groupby(s[0])[s[1]].count()
# 	for k in range(len(i)):
# 		try:
# 			print(str(k) + ' ' + str(i[k]))
# 		except: pass
#
# elif s[2] == 'min':
# 	i = people.groupby(s[0])[s[1]].min()
# 	for k in range(len(i)):
# 		try:
# 			print(str(k) + ' ' + str(i[k]))
# 		except: pass
#
# elif s[2] == 'max':
# 	i = people.groupby(s[0])[s[1]].max()
# 	for k in range(len(i)):
# 		try:
# 			print(str(k) + ' ' + str(i[k]))
# 		except: pass

"""
# Задача 3
# В данной задаче необходимо определить долю выживших людей ("Survived" == 1) в наборе данных,
# которые удовлетворяют заданному составному фильтру:
#
# 1    Их возраст ("Age") строго больше заданного числа N
# 2    Их Pclass строго равен заданному числу P
# 3    Количество родственников ("Parch") строго равно заданному числу K
"""

import pandas as pd

people = pd.read_csv("titanic.csv")
s = input().split()

age = s[0]
p_cls = s[1]
rel_num = s[2]

count_surved = 0
count_surved_filt = 0

age_survived = people.loc[people["Age"] > float(age)]
pclass_age_survived = age_survived.loc[people["Pclass"] == int(p_cls)]
rel_survived = pclass_age_survived.loc[people["Parch"] == int(rel_num)]


for i in rel_survived["Survived"]:
	count_surved_filt += i
	count_surved += 1

answer = count_surved_filt / count_surved
if answer == 0.0:
	print(0)
elif answer % 1 == 0:
	print(float("{0:.0f}".format(answer)))
else:
	print(float("{0:.4f}".format(answer)))




