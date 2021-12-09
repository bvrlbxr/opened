

# Измените данный код так, чтобы исключить дублирование кода, но, чтобы результат работы программы не изменился.
# Данное решение оценивается в баллах - чем меньше строк и символов в итоговом решении, тем больше баллов.
# Для получения максимального количества баллов, нужно, чтобы в решении было меньше 10 строк и меньше 350 символов,
# однако, данную задачу возможно решить в 175 символов и в 1 строку.


def get_people_with_min_age(people):
    m = 100000000000
    for p in people:
        if p["age"] < m:
            m = p["age"]

    names = []
    for p in people:
        if p["age"] == m:
            names.append(p["name"])

    for i in range(len(names)):
        for j in range(len(names)):
            if i < j:
                if names[i] > names[j]:
                    names[i], names[j] = names[j], names[i]

    return names

def get_people_with_max_age(people):
    m = -100000000000
    for p in people:
        if p["age"] > m:
            m = p["age"]

    names = []
    for p in people:
        if p["age"] == m:
            names.append(p["name"])

    for i in range(len(names)):
        for j in range(len(names)):
            if i < j:
                if names[i] > names[j]:
                    names[i], names[j] = names[j], names[i]

    return names

def get_people_with_min_height(people):
    m = 100000000000
    for p in people:
        if p["height"] < m:
            m = p["height"]

    names = []
    for p in people:
        if p["height"] == m:
            names.append(p["name"])

    for i in range(len(names)):
        for j in range(len(names)):
            if i < j:
                if names[i] > names[j]:
                    names[i], names[j] = names[j], names[i]

    return names


def get_people_with_max_height(people):
    m = -100000000000
    for p in people:
        if p["height"] > m:
            m = p["height"]

    names = []
    for p in people:
        if p["height"] == m:
            names.append(p["name"])

    for i in range(len(names)):
        for j in range(len(names)):
            if i < j:
                if names[i] > names[j]:
                    names[i], names[j] = names[j], names[i]

    return names

def get_people_with_min_weight(people):
    m = 100000000000
    for p in people:
        if p["weight"] < m:
            m = p["weight"]

    names = []
    for p in people:
        if p["weight"] == m:
            names.append(p["name"])

    for i in range(len(names)):
        for j in range(len(names)):
            if i < j:
                if names[i] > names[j]:
                    names[i], names[j] = names[j], names[i]

    return names


def get_people_with_max_weight(people):
    m = -100000000000
    for p in people:
        if p["weight"] > m:
            m = p["weight"]

    names = []
    for p in people:
        if p["weight"] == m:
            names.append(p["name"])
    for i in range(len(names)):
        for j in range(len(names)):
            if i < j:
                if names[i] > names[j]:
                    names[i], names[j] = names[j], names[i]
    return names





# print(get_people_with_max_weight(data))

# =========================  refactored ==========

def get_people_with_min_age2(people):
    return sorted([i['name'] for i in people if i['age'] == min(i['age'] for i in people)])

def get_people_with_max_age2(people):
    return [i['name'] for i in people if i['age'] == max(i['age'] for i in people)]

def get_people_with_min_height2(people):
    return [i['name'] for i in people if i['height'] == min(i['height'] for i in people)]

def get_people_with_max_height2(people):
    return [i['name'] for i in people if i['height'] == max(i['height'] for i in people)]

def get_people_with_min_weight2(people):
    return [i['name'] for i in people if i['weight'] == min(i['weight'] for i in people)]

def get_people_with_max_weight2(people):
    return [i['name'] for i in people if i['weight'] == max(i['weight'] for i in people)]


w1 = {'name': 'Gera', 'weight': 65}
w2 = {'name': 'Tema', 'weight': 80}
w3 = {'name': 'Lesha', 'weight': 75}
data = [w1, w2, w3]

a1 = {'name': 'Gera', 'age': 27}
a2 = {'name': 'Tema', 'age': 27}
a3 = {'name': 'Lesha', 'age': 27}
a3 = {'name': 'Lesha', 'age': 27}
a3 = {'name': 'Lesha', 'age': 27}
a3 = {'name': 'Lesha', 'age': 27}
data_age = (a1, a2, a3)

print(get_people_with_min_age(data_age))

print(get_people_with_min_age2(data_age))