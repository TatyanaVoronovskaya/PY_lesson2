# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.

n = int(input(f'введите количество элементов первого множества '))
m = int(input(f'введите количество элементов второго множества '))
list_n = []
list_m = []
for i in range(n):
    list_n.append(int(input(f'введите {i+1} элемент первого множества ')))
    i += 1
for j in range(m):
    list_m.append(int(input(f'введите {j+1} элемент второго множества ')))
    j += 1
print(f'первое множество : {list_n} ')
print(f'второе множество : {list_m} ')
set_list_n = set(list_n)
set_list_m = set(list_m)
list_n2 = list(set_list_n)
list_m2 = list(set_list_m)
new_list = []
for i in range(len(list_n2)):
    for j in range(len(list_m2)):
        if list_n2[i] == list_m2[j]:
            new_list.append(list_n2[i])

for i in range(0, len(new_list)-1):
    mini = i
    for j in range(i + 1, len(new_list)):
        if new_list[j] < new_list[mini]:
            mini = j
    new_list[i], new_list[mini] = new_list[mini], new_list[i]
print(new_list)

# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. 
# Она растёт на круглой грядке, причём кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них 
# выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, к
# оторое может собрать за один заход собирающий модуль, находясь перед некоторым .
# кустом заданной во входном файле грядки.

n = int(input(f'введите количество кустов '))
import random
list_1 = []
for i in range(n):
    temp = random.randint(0, 10) 
    list_1.append (temp)

print(list_1)
sum = 0
for i in range(-1, n-1):
    sum_i = list_1[i-1] + list_1[i] + list_1[i+1]
    if (sum_i > sum):
        sum = sum_i
    i += 1
print(f' S= {sum}')


