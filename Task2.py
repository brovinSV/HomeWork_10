"""
Напишіть програму, яка б приймала список з числами та перевіряла чи всі числа
в ньому унікальні. Реалізуйте у функції декілька обробок виключень.
"""

def unique(lst):
   for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j]:
                return print("Є однакові")
   return print("Усі елементи унікальні")

def unique_error(lst):
    try:
        return unique(lst)
    except TypeError as type_error:
        print(type_error, 'Wrong object type')

#my_list = [1, 4, 6, 8, 9, 4]
my_list = False
unique_error(my_list)
