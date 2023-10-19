def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# Пример использования
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17]
target = 17
result = binary_search(arr, target)

if result != -1:
    print(f"Искомый элемент {target} найден в массиве, индекс: {result}")
else:
    print(f"Искомый элемент {target} не найден в массиве")
