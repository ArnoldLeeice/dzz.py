#Задайте список из нескольких чисел.
#Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

a = input()
b = a.split()
c = [int(item) for item in b]
new_list = []
for i in range(len(c)):
    if i % 2 == 1:
        new_list.append(c[i])
print(sum(new_list))

#Напишите программу, которая найдёт произведение пар чисел списка.
#Парой считаем первый и последний элемент, второй и предпоследний и т.д.

a = input()
b = a.split()
c = [int(item) for item in b]
new_list = []
while len(c) > 0:
    res = c[0] * c[-1]
    new_list.append(res)
    c.pop(0)
    c.pop(-1)
    if len(c) < 2:
        sr = c[0]**2
        new_list.append(sr)
        c.pop(0)
print(new_list)

#Задайте список из вещественных чисел.
#Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

n = input()
b = n.split()
result = [float(item) for item in b]
result.sort()
res = []
for i in result:
    a = int(i)
    raz = i - a
    res.append(raz)
mn = min(res)
mx = max(res)
mx_new = str(mx)
mx_new2 = mx_new[:4]
print(mx_new2)

#Напишите программу, которая будет преобразовывать десятичное число в двоичное.

a = int(input())
b = bin(a)
res = str(b)
res1 = res[2:]
print(res1)

#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

f1 = f2 = 1
n = int(input())
print(f1, end=' ')
if n != 1:
    print(f2, end=' ')
for i in range(2, n):
    f1, f2 = f2, f1 + f2
    print(f2, end=' ')