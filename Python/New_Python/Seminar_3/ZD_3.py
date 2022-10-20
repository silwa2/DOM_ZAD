# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list = []
list2 = []

number = int(input("Введите число элементов: "))

for i in range(number):
    list.append(float(input("Введите элемент: ")))

for i in range(len(list)):
    number = list[i] % 1
    if number != 0:
        list2.append(number)

maxim = max(list2)
minim = min(list2)
print (maxim - minim)