def bubble_sort_imperative(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# Пример использования:
my_list = [64, 34, 25, 12, 22, 11, 90]
bubble_sort_imperative(my_list)
print(my_list)  # Выведет: [11, 12, 22, 25, 34, 64, 90]


# __________________________________________________________
def bubble_sort_declaration(arr):
    while True:
        swapped = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        if not swapped:
            break


# Пример использования:
my_list = my_list.copy()
bubble_sort_declaration(my_list)
print(my_list)  # Выведет: [11, 12, 22, 25, 34, 64, 90]
