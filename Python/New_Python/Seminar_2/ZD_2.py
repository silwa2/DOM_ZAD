# 2) Напишите программу, которая принимает на вход число N 
# и выдает набор произведений чисел от 1 до N.

# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)



from symbol import factor
import sys

while True:
    n = int(input('Введите число N = '))
    number = 1
    
    if n < 0:
            print ("Введите положительное число.")
            sys.exit()
    def factorial(number):
    
            for i in range(n):
                    i += 1
                    number *= i
            return number
    
    print(factorial(number), end=" ")
    print ('\n') 
    

