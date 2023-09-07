def array_arithmetic_progression_filling(my_array, a1, step, n):
    for i in range (n):
        my_array.append(a1 + (i * step))
    return my_array
        
a1 = int(input('Введите 1й элемент прогрессии: '))
step = int(input('Введите шаг прогрессии: '))
n = int(input('Введите количество элементов прогрессии: '))
arithmetic_progression = []

print(array_arithmetic_progression_filling(arithmetic_progression, a1, step, n))