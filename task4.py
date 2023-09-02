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