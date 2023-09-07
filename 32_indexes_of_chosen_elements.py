def array_creation(n, el_min, el_max):
    import random
    array = []
    for i in range(n):
        array.append(random.randint(el_min, el_max))
    return array

def indexes_of_chosen_elements(array, min_border, max_border):
    indexes = []
    for i in range(len(array)):
        if min_border <= array[i] <= max_border:
            indexes.append(i)
    return indexes

chosen_min = int(input('Введите минимальное значение элемента: '))
chosen_max = int(input('Введите максимальное значение элемента: '))
my_array = array_creation(6, 1, 20)

print(my_array)

print(indexes_of_chosen_elements(my_array, chosen_min, chosen_max))