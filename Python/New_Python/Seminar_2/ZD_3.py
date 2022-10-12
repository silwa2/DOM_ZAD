# 3) Задайте список из n чисел последовательности (1 + 1/n)^n 
# и выведите на экран их сумму.

# *Пример:*
#     Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}
#     Сумма 9.06

n = int(input('Введите количество чисел N: '))

def number(n):
    summa = 0
    for i in range(n):
        chislo = int(input(f'Введи число {i + 1} -> '))
        chislo = (1+1/chislo)**chislo
        summa += chislo
        i += 1
    return summa

print('Сумма чисел = ',round((number(n)), 2))