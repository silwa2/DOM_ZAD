# 5) Реализуйте алгоритм перемешивания списка.

from csv import list_dialects
from random import Random, randint

n = int(input('Введите количество элементов списка: '))
spisok = []

for i in range(n):
    spisok.append(randint(-n,n))
print(spisok)

def new_spisok(spisok):
    list = spisok[:]
    
    for i in range(len(list)):
        index = randint(0, len(list) - 1)
        temp = list[i]
        list[i] = list[index]
        list[index] = temp
    return list
    
print(new_spisok(spisok))