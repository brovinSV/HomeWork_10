"""
Напишіть користувацький клас виключення з функционалом на свій вибір.
Викличте його за допомогою інструкції raise.
"""

class MyError(Exception):
    def __init__(self, text, num):
        self.txt = text
        self.n = num

number = input("Input positive integer: ")

try:
    number = int(number)
    if number < 0:
        raise MyError("You give negative!", number)
except ValueError:
    print("Error type of value!")
except MyError as mr:
    #print(mr)
    print(mr.args[0], mr.args[1])
else:
    print(number)