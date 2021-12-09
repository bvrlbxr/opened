# import sqlite3
# import json
#
# con = sqlite3.connect('db.sqlite')
# cur = con.cursor()
#
#
# row = cur.execute('SELECT * FROM films WHERE director= " Эльдар Рязанов" AND year < 1970')
# for i in row:
#         print(i)
#
#
#
# struct = json.loads('{" Эльдар Рязанов": [{"Берегись автомобиля ": {"год выхода": "1966", "рейтинг фильма": "8.167"}}]}')
# print(struct)
#
#
#
# with open('data.json', 'w', encoding='utf-8') as outfile:
#     json.dump('{" Эльдар Рязанов": [{"Берегись автомобиля ": {"год выхода": "1966", "рейтинг фильма": "8.167"}}]}', outfile, ensure_ascii=False)
#
#
#
# row = cur.execute('SELECT * FROM films')
# for i in row:
#         print(i)


from pymongo import MongoClient

# client = MongoClient('127.0.0.1', 27017)
# db = client.sample_weatherdata
# collection = db.data
#
# data = collection.find()
#
# count = 0
# for i in data:
# 	if i['pressure']['value'] < 1000.0:
# 		count += 1
#
# print(count)


# client = MongoClient('127.0.0.1', 27017)
# db = client.sample_restaurants
# collection = db.restaurants
#
# data = collection.find()
#
# count = 0
# for i in data:
# 	if i['borough'] == 'Bronx' and 'Food' in i['name']:
# 		print(i['borough'] + ' ' + i['name'] + '===' + i['cuisine'])
# 		count += 1
# print(count)

# client = MongoClient('127.0.0.1', 27017)
# db = client.sample_supplies
# collection = db.sales
#
# data = collection.find()
#
# # 'customer': {'gender': 'M', 'age': 42
# count = 0
# age = []
# for i in data:
# 	age.append(i['customer']['age'])
#
# print(str(min(age)) + ', ' + str(max(age)))

def get_ages_sum():

	client = MongoClient('127.0.0.1', 27017)
	db = client.db
	collection = db.users

	data = collection.find()

	age = 0
	for i in data:
		age += i['age']

	return age

print(get_ages_sum())