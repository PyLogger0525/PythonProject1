# a = float(input('Длина комнаты: '))
# if a <= 4:
#     print(a, 'метра')
# else:
#         print(a, 'метров')
# b = float(input('Ширина комнаты: '))
# if b <= 4:
#     print(b, 'метра')
# else:
#     print(b, 'метров')
# s = a * b
# print('Площадь комнаты = ', s)

# akr = 43560
# a = float(input('Длина участка (футы)'))
# b = float(input('Ширина участка (футы)'))
# sakr = (a * b) / akr
# print(sakr, 'акров')

# a = 0.10
# b = 0.25
# l1 = float(input('Бутылок объемом 1 л и меньше: '))
# l2 = float(input('Бутылок бъемом больше 1 литра: '))
# cash = (l1 * a) + (l2 * b)
# allcash = round(cash, 2)
# print(allcash, "$")

# nalog_proc = 0.13
# stuff_cash = 0.18
# sum_food = float(input('Итог чека:'))
# nalog = sum_food * nalog_proc
# stuff = sum_food * stuff_cash
# print('Итог: ', sum_food, '\nНалог: ', nalog, '\nЧаевые: ', stuff)


# pr = 0.75
# bz = 1.12
# all_pr = float(input('Количество сувениров: '))
# all_bz = float(input('Количество безделушек: '))
# all_result = (pr * all_pr) + (bz * all_bz)
# print('Общий вес посылки: ', all_result, 'килограмм')

# proc = 4
# start = int(input('Введите сумму открытия депзита: '))
# year_1 = round(((start * 365 * 4) / 36500) + start)
# year_2 = round(((year_1 * 365 * 4) / 36500) + year_1)
# year_3 = round(((year_2 * 365 * 4) /36500) + year_2)
# print('Сумма с процентами за 1 год:', year_1, '\nСумма с процентами за 2 год:', year_2, '\nСумма с процентами за 3 год:', year_3)


# a = int(input('Количество сувениров: '))
# b = int(input('Количество безделушек: '))
# all = round(((a * 0.75) + (b * 0.112)), 2)
# print('Общий вес посылки: ', all)

# mpg = int(input('MPG: '))
# Km = round((235.22/mpg),2)
# print(Km, 'L/100km')

# coin = [1, 2, 5, 10, 25, 100, 200]
# sum = input()
# if sum := 0:
#     print()

# numbers = '1 2 3 4 5 6 7'
# numbers_split = numbers.split() # список цветов по-отдельности
# for number in numbers_split:
#     print(number)
# pi = 31.4159265
# print ("%.4e" % (pi))


# h = 1
# m = 2
# s = 3
# print("%02d:%02d:%02d" % (h, m, s))

# L = ["а", "б", "в", 1, 2, 3, 4]
# print (L[1:4])
# # ["б", "в", 1]

# L = ["а", "б", "в", 1, 2, 3, 4]
# print (L[::3])
# # ["а", 1, 4]

# L = ["а", "б", "в", 1, 2, 3, 4]
# print (L[-4::-1])
# # [1, "в", "б", "а"]

# L = ["а", "б", "в", 1, 2, 3, 4]
# print (L[:-4:-1])
# # [4, 3, 2]
# L = [3.3, 4.4, 5.5, 6.6]
# print(map(round, L))
# print(list(map(round, L)))

# L = ['3.3', '4.4', '5.5', '6.6']
# print(map(round, L))
# print(list(map(round, L)))
#
# L = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# # L = input('Введите числа: ')
# L_2 = list(map(int, input().split())) #почему надо в list вместе с split писать input()??
# L[0], L[-1] = L[-1], L[0]
# L.append(sum(L))
# print(L)

# d = {'day' : 22, 'month' : 6, 'year' : 2015}
# print("||".join(d.keys()))

# title = input()
# author = input()
# year = input()
# # book = {'title' : 'Идиот', 'author' : 'Достоевский Ф.М.', 'year': 1869}
# book = {'title' : title, 'author' : author, 'year' : int(year)}
# print(book)

# Tekst = "The Zen of PythonBeautiful is better than ugly.Explicit is better than implicit.Simple is better than complex.Complex is better than complicated.Flat is better than nested.Sparse is better than dense.Readability counts.Special cases aren't special enough to break the rules.Although practicality beats purity.Errors should never pass silently.Unless explicitly silenced.In the face of ambiguity, refuse the temptation to guess.There should be one-- and preferably only one --obvious way to do it.Although that way may not be obvious at first unless you're Dutch.Now is better than never.Although never is often better than *right* now.If the implementation is hard to explain, it's a bad idea.If the implementation is easy to explain, it may be a good idea.Namespaces are one honking great idea -- let's do more of those!"
# print(Tekst.split())
# c = list(set(Tekst))
# print(len(c))

# a = input("Введите первую строку: ")
# b = input("Введите вторую строку: ")
# a_set, b_set = set(a), set(b) # используем множественное присваивание
# a_and_b = a_set.intersection(b_set)
# print(a_and_b)

# e = input()
# a = input()
# e_set, a_set = set(e), set(a)
# e_a = e_set.symmetric_difference(a_set)
# print(e_a)
#
# a = input("Введите первую строку: ")
# b = input("Введите вторую строку: ")
# a_set, b_set = set(a), set(b) # используем множественное присваивание
# a_and_b = a_set.symmetric_difference(b_set)
# print(sorted(a_and_b))
# L = ['a', 'b', 'c']
# print(id(L))
#
# L.append('d')
# print(id(L))

# a = 5
# b = 3+2
# print(id(a))
# print(id(b))

# shopping_center = ("Галерея", "Санкт-Петербург", "Лиговский пр., 30", ["H&M", "Zara"])
# list_id_before = id(shopping_center[-1])
#
# shopping_center[-1].append("Uniqlo")
# list_id_after = id(shopping_center[-1])
# print(list_id_before == list_id_after)

# password = "dgh36gh7"
# answer = input()
# #место для написания кода
# if answer == password:
#     print(True)
# else:
#     print(False)
#можно было проще: print(password == answer)

# person_age = int(input())
# if person_age >= 18 and person_age <= 35:
#     print(True)
# else:
#     print(False)
# #можно было проще: print((person_age >= 18) and (person_age <= 35))

# a = 23
# b=str(a)
# f_e=int(b[0])
# print(f_e % 2 == 0)

# fruits = ['apple', 'banana', 'cherry']
# f_f=fruits.pop()
# print(f_f)

# S = (123456789)
# print('3' and '7' in str(S))

# list_1 = [1, 2]
#
# list_2 = [1, 2, 3]
# val = list_2.pop()
#
# print(id(list_1) == id(list_2))

# heads = 35  # количество голов
# legs = 94  # количество ног
#
# for r in range(heads + 1):  # количество кроликов
#     for ph in range(heads + 1):  # количество фазанов
#         #  если суммарное количество голов превышено или ног превышено, то переходим на следующий шаг цикла
#         if (r + ph) > heads or \
#             (r * 4 + ph * 2) > legs:
#             continue
#         if (r + ph) == heads and (r * 4 + ph * 2) == legs:
#             print("Количество кроликов", r)
#             print("Количество фазанов", ph)
#             print("---")

# list_ = [1,2,3,-1,3,2,1,2,3,2,1,0,0,0,-1,2]
# #2
# negate_index = -1
# #3
# negate_value = 0
# #4
# for i, val in enumerate(list_):
# #5
#    if val < 0:
#        #6
#        negate_index = i
#        #7
#        negate_value = val
#        break
#
# print(f'{negate_index}: {negate_value}')


##чтобы при переборе всех чисел от 1 до 99 выводилось “число % 3”, если число кратно 3; “число % 5”, если число кратно 5; при этом все четные числа бы игнорировались

# for i in range(1,100):
#     if i % 2 == 0:
#         continue
#     if i % 3 == 0:
#        print (f'{i} % 3')
#     if i % 5 == 0:
#        print (f'{i} % 3')

# numbers = [2,8,22,88,21,16,18,12,0,77,12,32,43,54,12]
# for n in numbers:
#     if n==0:
#         break
#         print("Нельзя произвести вычисление")
# print(n)

#Дано n-значное целое число N. Определите, начинается ли оно с чётной цифры.
# i=55468
# s=str(i)
# s_1=int(s[0])
# if s_1 % 2==0:
#     print('True')
# else:
#     print("False")

# def hello_world():
#     print('Hello World')
# hello_world()

# def pow_func(a, n):
#     if a%n == 0:
#         print('является')
#     else:
#         print('не является')
# pow_func(9, 3)

# def ob_l(n):
#     for i in range(n, 0, -1):
#         for j in range(i, 0, - 1):
#             print(j, end = '')
#         print()
# ob_l(4)

# n = 4
# for i in range(n):
#     for j in range(1, i + 2):
#         print(j, end = '')
#     print()
# n = 3
# for i in range(1, n +1):
#     print(str(i) * i)



# def func():
#    global x # объявляем, что переменная является глобальной
#    print(x)
#    x = 5
#    x += 5
#    return x


# def add(*nums):
#    sum=1
#    for n in nums:
#       sum=sum*n
#    return sum
# print(add(2, 2))


# def incorrect_func(name_arg=[]):
#    # name_arg является локальной переменной
#    print("Аргумент до изменения", name_arg)
#    name_arg.append(1)
#    print("Аргумент после изменения", name_arg)
#
# # вызовем два раза одну и ту же функцию
# incorrect_func()
# print('-----')
# incorrect_func()
# print('-----')
# incorrect_func()

# def count(start=1, step=1):
#    counter = start
#    while True:
#       yield counter
#       counter += step
# cnt= count(start=5, step=2)
# for v in cnt:
#       print(v)

# def repeat_list(list_):
#    list_values = list_.copy()
#    while True:
#        value = list_values.pop(0)
#        list_values.append(value)
#        yield value
#
# for i in repeat_list([1, 2, 3]):
#    print(i)
#
# Счетчик увеличивающийся на единицу при каждом вызове на экран

# def counter(start):
#     def step():
#         nonlocal start # объявляем переменную start как не локальную, чтобы брать значение из основной (внешней) функции и не задавать значение переменной повторно в подфункции что также,
#                         # является связью между функциями.
#         start+=1
#         return start # объявляем возврат результата выплонения операции во вложенной функции для записи ее значения и дальнейшего использования,
#                     # иначе результат удаляется (аналог 'print' в функциях)
#
#     return step # объявляем возврат результата вложенной функции для подтягивания значения в основную и для доступа к ней в дальнейшем
                # То есть, делаем ссылку на результат выполнения вложенной функции и выполняем запись чтобы основная функция выдала результат.

# c= counter(10) # 'c' это переменная ссылающаяся на функцию (так выполняется замыкание функций), то есть,
#                # 'c' объединяет все функции и заставляет выполняться их циклично и работать как счетчик. Без 'c'=counter() невозможно выполнение алгоритма счетчика, вывод конечного итога невозможен.
#
# c1=counter(1) # то же самое, просто добавляем второй запрос с другим значением переменной (выводится вторым столбцом). Можно не писать если не нужно.
# # 'c' - то есть, это независимое локальное окружение где выполняются все связанные функции с указанным параметром
# print(c(), c1())
# print(c(), c1())
# print(c(), c1())

# ЗАДАЧА НА НАПИСАНИЕ ДЕКОРАТОРА И ПРИМЕНЕНИЕ ЭТОГО ДЕКОРАТОРА К ФУНКЦИИ
# ДЕКОРАТОР №1 ДЛЯ ОПРЕДЕЛЕНИЯ ВРЕМЯ ВЫПОЛНЕНИЯ ФУНКЦИИ

# import time     # импорт модуля time до написания тела программы или функции который позволит использовать команду " ".time
#
# def test_time(func):
#     def wrapper(*args, **kwargs):   # *args **kwargs задаем если заранее не знаем значений параметров, делаем функцию универсальной
#         print('Текущее время: ', time.strftime("%H:%M:%S", time.localtime()))    # команда для вывода текущего времени (до выполнения функции)
#         print('Запустилась функция func')
#         st=time.time()      # применяем команду для определения текущего времени системы
#         res=func(*args, **kwargs)       # распаковка и передача параметров
#         et=time.time()      # применяем команду для определения текущего времени системы после выполнения команды
#         print('Текущее время: ', time.strftime("%H:%M:%S", time.localtime()))
#         dt=et-st        # находим разницу между временем до и после выполнения команды
#
#         print(f"Время работы: {dt:.10f} сек") # Так как время выполнения программы очень мало, делаем форматирование числа dt с указанием 10 знаков после запятой (суффикс f). Для этого в f-строке
#                                             # добавляется двоеточие, точка, количество десятичных знаков и суффикс f в конце.
#
#         return res      # возвращаем результат выполнения функции func по параметрам (*args, **kwargs) для дальнейшего вывода этих данных в тело вложенной функции, если не указать return, значения не выведутся
#                         # при обращении, т.к. итог выполнения команды не будет записан.
#     return wrapper      # делаем  ссылку на результат выполнения вложенной функции, т.е. записываем значение в тело функции wrapper

# ДЕКОРАТОР №2 ДЛЯ ПОДСЧЕТА КОЛИЧЕСТВА ВЫЗОВОВ ОДНОЙ ФУНКЦИИ. (ЗАДАНИЕ 5.5.2)

# def counter(cnt):
#     cnt1=0
#     def wrap(*args, **kwargs):
#         nonlocal cnt1
#         cnt(*args, **kwargs)
#         cnt1+=1
#         print(f"Функция {cnt.__name__} была вызвана {cnt1} раз")
#     return wrap
#
#
# @counter  # Прописываем декоратор (делаем ссылку) который хотим применить к этой функции
# def ob_l(n):
#     for i in range(n, 0, -1):
#         for j in range(i, 0, - 1):
#             print(j, end = '')
#         print()
# ob_l(2)
# ob_l(3)

# ДЕКОРАТОР №3 декоратор, который будет сохранять результаты выполнения декорируемой функции в словаре. (ЗАДАНИЕ 5.5.3)

# def dict1(dic):
#     dict2= {}
#     def wrap(args):
#         nonlocal dict2
#         if args not in dict2: # При каждом вызове проверять, не было ли уже аналогичного вызова, если с таким параметром вызов уже был
#             dict2[args] = dic(args)
#             print(f"Добавление результата в кэш: {dict2[args]}")
#         else:
#             print(f"Возвращение результата из кэша: {dict2[args]}")
#         print(f"Кэш {dict2}")
#         return dict2[args]
#     return wrap
#
# @dict1
# def f(n):
#    return n * 123456789
# print(f(1))
# print(f(1))

# Проверяем содержит ли цифру 5 число num, число в строку не переводим.

# num=5246
# s1=num // 1000  # целочисленное деление на тысячу для того чтобы найти первую цифру
# s2 = num // 100 %10 # делим на сто чтобы передвинуть запятую после второго знака в числе num и делим полученное на 10 с остатком, остаток от деления и есть ответ
# s3 = num // 10 % 10
# s4 = num // 1 %10
#
# while s1 != 5 and s2!= 5 and s3 != 5 and s4 != 5:
#     print(False)
#     break
# else:
#     print(True)


# num=5246
# s1=num // 1000  # целочисленное деление на тысячу для того чтобы найти первую цифру
# s2 = num // 100 %10 # делим на сто чтобы передвинуть запятую после второго знака в числе num и делим полученное на 10 с остатком, остаток от деления и есть ответ
# s3 = num // 10 % 10
# s4 = num // 1 %10
# i = int(input())
# while s1 !=i or s2 !=i:
#     print(False)
#     break
# else:
#     print(True)

# Найти макс значение в матрице

# test_matrix = [[1, 2, 3],
#               [7, -1, 2],
#               [123, 2, -1]]
#
# max = test_matrix[0][0] # берем в качестве точки отсчета любой элемент из матрицы
# for row in test_matrix:
#    for el in row:
#        # если элемент больше максимального, то это новый максимум
#        if el > max:
#            max = el
# print(max)

# n = 5
# for i in range(1, n):
#     for j in range (1, i+1):
#         print(j, end=" ")
#     # for k in range(1, j+1):
#     #     print(k, end = " ")
#     print()
# for i1 in range(1, n):
#     for j1 in range (1, i1+1):
#         print(j1, end=" ")
#     print()
#
# rows = 5  # Высота ёлочки
# i = 1  # Отслеживание текущего уровня
# while i < rows:
#     j = 1  # Отслеживание текущей позиции на каждом уровне
#     while j < i:
#         print("\*", end="")  # Напечатать символ «\*» на текущей позиции
#         j += 1  # Перейти к следующей позиции
#     print()  # Перейти на новую строку после печати всех символов до текущего уровня
#     i += 1  # Увеличить текущий уровень


# 5.2.3 Напишите функцию, которая проверяет, является ли число n делителем числа a и выводит на экран соответствующее сообщение, является ли число делителем или нет.
# def num(n, a):
#     print(f"",a%n==0) # записываем сразу в принт при помощи f строки выражение на проверку, делится ли число а на число n без остатка
# num(3, 17)

# Находим числитель числа.
# def num (a):
#     for i in range(1, a): # указываем диапазон где надо искать числители числа а. Ставим от одного чтобы был тип данных int, если указать без 1, то по умолчанию будет строковое значение.
#         if a%i==0:
#             s=i+(i+1)
#             print(s)
#     print()
# num (6)

# Находим кол-во числителей числа.
# def num (a):
#     cnt=0
#     for i in range(1, a+1): # указываем диапазон где надо искать числители числа а. Ставим от одного чтобы был тип данных int и +1 для того, чтобы и само число вошло в этот диапазон.
#         if a%i==0:
#             cnt+=1
#     print(cnt)
# num (4)

# 5.2.6 Напишите функцию, которая проверяет, является ли данная строка палиндромом или нет, и возвращает результат проверки.
# def check_palindrome(n):
#     n=str(n)
#     n = n.lower()
#     n = n.replace(" ", "")
#     n = n.replace("\n", "")
#     print(n[::1]==n[::-1])
# check_palindrome("test")
# check_palindrome("Кит на море не романтик")


# 5.3.2 Написать функцию, которая будет перемножать любое количество переданных ей аргументов
# def sum(*n): # ставим звездочку * для того, чтобы функция принимала не один параметр, а чтобы в n можно было подавать несколько параметров для вычисления
#     s = 1 # Создаем переменную s до тела функции, чтобы использовать ее как счетчик
#     for i in n:
#         s*=i
#         print(s)
# sum(5, 6, 8)

# def num(n):
#     for i in range(n, n+1):
#         while True:
#             n<n+1
#             yield n+1
# num(5)

# a = 5
# b = 3+2
# c=6
# while id(a) - id(b)==0 and id(a) - id(c)==0:
#     print('не найдено')
#     break
# else:
#     print(1)

# a = 0
# b = 0
#
# while id(a) == id(b):
#     a += 1
#     b += 1
# print(a)

# Напишите числа в порядке возрастания через пробел, которые выведет программа из предыдущего задания, если на вход подаются две последовательности чисел:
# Задание 7.2.12

# i = 5687
# j = 9851
# # b={i, j}
# b = set(str(i)).symmetric_difference(set(str(j))) # исключаем одинаковые символы, преобразуем int в строку, затем в множество. Т.к. int в множество нельзя преобразовать сразу.
# b1=sorted(b) # сортируем символы в строке по возрастанию
# print(list(b1)) # выводим в виде списка

#7.3.8

# проверяем введенное число на условия
# a = input()
# print(f'{"Число удовлетворяет условиям" if int and 100<int(a)<1000 and a % 2 ==0 and a%3==0 else 0}')

# те же самые условия (просто другой способ) только решение задачи с функцией all которая объединяет все условия и проверяет их выполнение сразу, это чтобы не писать множество if или не прописывать в print
# a=int(input())
# if all([type(a) == int,
#         100 <= a <= 999,
#         a % 2 == 0,
#         a % 3 == 0]):
#     print("Число удовлетворяет условиям")
# else:
#     print("Число не удовлетворяет условиям")



# L=[1,2,3,8,5]
# for i in L:
# L=[]
# if any([L % 2==0, L % 3==0]):
#     print(True)
# else:
#     print(0)


# результат будет истинным тогда и только тогда, когда в списке есть хотя бы один чётный и хотя бы один нечётный элемент.

# L = [int(input()) % 2 == 0 for i in range(3)]
# print(any(L) or not all(L)) #с помощью and создаем условие при котором True не будет выходить если все значения будут четными


# Задание 7.3.15
# Используя функцию zip() внутри генераторов списков, вычислите поэлементные произведения списков L и M.
# L = [i for i in range(10)]
# M = [i for i in range(10,0,-1)]
# S = [a*b for a,b in zip(L,M)]
# print(S)


# m = []
# m = {i:L1.count(i) for i in L1}
# print(m)

# def compress_string(s):
#     compressed = ""
#     count = 1
#     for i in range(1, len(s)):
#         if s[i] == s[i - 1]:
#             count += 1
#     else:
#         compressed += s[i - 1] + str(count)
#     count = 1
#     compressed += s[-1] + str(count)
#     return compressed
#
# L = 'aaabbccccda'
# L1=list(L)
# comp = compress_string(L)
# print(comp)

# for i in range(len(L1)-1):
#     c = str(L1.count(i))
#     m.append(c)
#     if i in m:
#         i=1
#         print(i, c)
# L2 = [x+i for x, i in zip(L1, m)]
# print(str(L2))

# def e():
#     n = 1
#     while True:
#         yield (1 + 1 / n) ** n
#         n += 1
#
# a = e()
# print(a)


def change_profile():
    print("Profile has been changed")

def has_access(func):
    def wrapper():
        if username in USERS:
            print("Авторизован как", username)
            func()
        else:
            print("Доступ пользователю", username, "запрещён")
    return wrapper

def is_auth(func):
    def wrapper():
        if auth:
            print("Пользователь авторизован")
            func()
        else:
            print("Пользователь не авторизован. Функция выполнена не будет")
    return wrapper

USERS = ['admin', 'guest', 'director', 'root', 'superstar']

yesno = input("""Введите Y, если хотите авторизоваться, или N, 
             если хотите продолжить работу как анонимный пользователь: """)

auth = yesno == "Y"

if auth:
    username = input("Введите ваш username:")

@is_auth
@has_access
def from_db():
    print("some data from database")
