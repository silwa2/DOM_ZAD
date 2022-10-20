# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


num = int(input("Введите целое число: "))

fibonacci = [0, 1]
otriz_fibonacci = [1, 0]

for i in range(2, num + 1):
    fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
    otriz_fibonacci.insert(0, otriz_fibonacci[1] - otriz_fibonacci[0])

if num == 0:
    print(0)
else:
    otriz_fibonacci.extend(fibonacci[1:])
    print (otriz_fibonacci)
