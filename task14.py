# Задача 14: Требуется вывести все целые степени двойки 
# (т.е. числа вида 2k), не превосходящие числа N

n=int(input("Введите максимальное число N: "))
p=1
while p <= n:
    print(p, ' ')
    p = p * 2