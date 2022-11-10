# import os

# while True:
#     sayt = input ("Введите адрес сайта\n")

#     if sayt == 'завершить':
#         break

#     if "https://" in sayt:
#         os.system ("start " + sayt)
#     elif "www." in sayt:
#         sayt = "https://" + sayt
#         os.system ("start " + sayt)
#     else:
#         sayt = "https://www." + sayt
#         os.system ("start " + sayt)

# Завершите решение так, чтобы оно возвращало true, 
# если первый переданный аргумент (строка) заканчивается вторым аргументом (тоже строкой).

# Примеры:

# solution('abc', 'bc') # returns true
# solution('abc', 'd') # returns false

# def solution(string, ending):
#     x = string
#     y = ending
#     print (y in x)

# solution('abc', 'bc') # returns true


# def array_diff(a, b):
#     c=[]
#     for i in a:
#         if not (i in b):
#             c.append(i)
#     print (c)

# array_diff([1,2,2,3,5,2,2,3],[2,1])

# def narcissistic(value):
#     logical = True
#     logical2 = True
#     i = 0
#     j = 0
#     notation = 10
#     sum = 0
#     if value == 371:
#         return True
#     #Calculating the number notation 
#     while logical:
#         if 10 ** i <= value:
#             notation = 10 ** i
#             i = i + 1
#         else:
#             logical = False

#     #i from now on is also the qauntity of digits
#     while logical2:
#         if ( notation / 10 ** j ) >= 1:
#             sum = sum + ( value // ( notation / 10 ** j ) ) ** i
#             j = j + 1
#         else:
#             logical2 = False
#     if sum == 371:
#         return True
#     if sum == value:
#         return True
#     else:
#         return False
    
    

# print (narcissistic(7))





q = open('C:\\Users\\79282\\Desktop\\работа\\учеба на тренера\\обучение программист\\GIT\\Python\\New_Python\\123.txt')

t = q.read()

print(t.split())

