def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

arr = [1, 3, 7, 8, 9, 5]
target = 7
result = binary_search(arr, target)

print(f"Cписок: {arr}")
print(f"Цель: {target}")

if result == -1:
    print("Элемент не найден")
else:
    print(f"Элемент найден по индексу {result}")