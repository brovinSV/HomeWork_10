"""
Напишіть функцію, яка б приймала номер місяця, а вертала його
назву. Реалізуйте у функції декілька обробок виключень.
"""


def month_name(num):
    name = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september',
            'october', 'november', 'december']
    try:
        return print(name[num - 1])
    except (TypeError):
        print("Wrong type passed to function")
    except (ValueError):
        print("Invalid value argument")
    except (IndexError):
        print("You tried to take an index that is not in the list")

month_name(13)