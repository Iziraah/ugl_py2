# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. 
# Для проверки своего кода используйте модуль fractions.

num1 = input('Введите первую дробь в видe "a/b": ').split('/')
num2 = input('Введите вторую дробь в видe "a/b": ').split('/')

# print(num1)
# print(int(num1[0])+int(num1[1]))
def sum():
    chislitel = int(num1[0])*int(num2[1])+int(num2[0])*int(num1[1])
    znamenatel = int(num1[1])*int(num2[1])
    return print(f'{chislitel}/{znamenatel}')

def multipl():
    chislitel = int(num1[0])*int(num2[0])
    znamenatel = int(num1[1])*int(num2[1])
    return print(f'{chislitel}/{znamenatel}')
vibor = int(input("что будем делать? \n 1 - сложение; \n 2 - умножение. \n"))
if vibor == 1:
    sum()
else:
    multipl()