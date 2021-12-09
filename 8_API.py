# Задача 1
# Используя API (https://the-one-api.dev/documentation) ответить,
# сколько глав в книге “Две крепости” и сколько всего персонажей в целом.
# Ответ вывести через запятую без пробелов. Для запроса по персонажам потребуется получить токен.
# Для этого нужно зарегистрироваться на сайте и выполнить вход, токен будет на странице.

# Пример ответа с токеном:
# token = "MY-TOKEN"
# res = requests.get(url, headers={"Authorization":f"Bearer {token}"}).json()
# Пример ответа: 9,500



# 1. Узнаем id книги с помощью запроса /book, id  = 5cf58077b53e011a64671583
# 2. 21 глава
# 3. 933 персонажа
import requests

# token = "aotIEuOKc_llqyBfKXS-" # мой токен с сайта
# url = 'https://the-one-api.dev/v2/character'
# res = requests.get(url, headers={"Authorization":f"Bearer {token}"}).json()
# print(res)


# Задача 2
# Используя API (https://pokeapi.co/docs/v2) вывести через запятую имя покемона под id 35 и его способности.
#
# Пример ответа (для покемона под номером 5): 'charmeleon', 'blaze', 'solar-power'


url = 'https://pokeapi.co/api/v2/pokemon/35'
res = requests.get(url).json()
print(res['name'], *[x['ability']['name'] for x in res['abilities']])
