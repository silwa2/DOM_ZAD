# 1) Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# *Пример:*
# - 6782 -> 23
# - 0,56 -> 11



number = input("Введите число: ")

def summa_numbers(number):                            
    if float(number) < 0:                         
        number = float(number) * -1
    number_new = 0

    for i in str(number):
        if i != '.':
            number_new += int(i)
    return number_new

print (summa_numbers(number))