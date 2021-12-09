# ! Дописать return!!
# !! Дописать условия задач!!
#  задача 4

def elochka(s):
    s = input()
    for i in s:
        print(s)
        s = ' ' + s

#  задача 5


def bigletters(s):
    #s = input()
    print(s.title())

#  задача 6


def countchars(s):
    #s = str(input())
    count_new = 0
    b = ''

    for i in s:
        count = 0
        for j in s:
            if j == i:
                count = count + 1

        if count > count_new:
            count_new = count
            b = i
    # по-хорошему еще нужен обработчик одинакового количества вхождений
    print(b)

#  задача 7 фибоначи


def fibona4(n):
    #n = int(input())
    fib1 = 1
    fib2 = 1
    i = 0
    while i < n - 2:
        fib_sum = fib1 + fib2
        fib1 = fib2
        fib2 = fib_sum
        i = i + 1

    print(fib2)


