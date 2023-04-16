# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#    1 2 3 4 5
#    3
#    -> 1

N = int(input('Введите количество элементов в массиве: '))
A = list(range(N))
A.append(N)  # добавить значение, которое равно N
A.remove(0)  # удалить значение 0 в массиве
print(*A)
X = int(input('Введите число, которое необходимо найти в массиве: '))
num=0
for i in range(N):
    if A[i] == X:
        num+=1
print(f'Число {X} встречается в массиве {num} раз')
