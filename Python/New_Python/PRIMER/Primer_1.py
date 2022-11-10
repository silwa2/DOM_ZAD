# Задача 2
# записать в 2 файла:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89];
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13].
# Нужно вернуть список, который состоит из элементов, общих для этих двух списков в новом файле.

with open ('text1.txt', 'w', encoding='utf-8') as data:
    data.writelines('1, 1, 2, 3, 5, 8, 13, 21, 34, 96, 89, 1')
    
with open ('text2.txt', 'w', encoding='utf-8') as data:
    data.writelines('1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 96, 11, 12, 13, 1')
    
with open ('text1.txt', 'r', encoding='utf-8') as data:
    dataWan = list(data.read().split(','))
    print (dataWan)

with open ('text2.txt', 'r', encoding='utf-8') as data:
    dataTwo = list(data.read().split(','))
    print (dataTwo)


result = list(filter(lambda elem: elem in dataWan, dataTwo))
y=list(map(int, result))
y.sort()
print(y)

with open('text3.txt', 'w', encoding= 'utf-8') as data:
    data.writelines(str(y))



