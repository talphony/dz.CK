import random
import time


def sort_bubble (arr):
    size = len(arr)
    for i in range(size):
        for j in range(0, size - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def sort_quick (arr):
    if len(arr) <= 1:
        return arr
    else:
        support = random.choice(arr)
        right = []
        central = []
        left = []
        for elem in arr:
            if elem > support:
                left.append(elem)
            elif elem == support:
                central.append(elem)
            elif elem < support:
                right.append(elem)
    return sort_quick(right) + central + sort_quick(left)

sizeArr = 10000
array = [i for i in range(sizeArr)]
for i in range(sizeArr):
  array[i] = random.randint(0, 99)

array_cp = array[:]

print("Исходный массив")
print(array_cp)
print('\n')

print("Пузырьковая сортировка")
sort_bubble_time_start = time.time()
sort_bubble(array_cp)
sort_bubble_time_end = time.time()
sort_bubble_time = sort_bubble_time_end - sort_bubble_time_start
print("Время пузырьковой сортировки", sort_bubble_time)
print(sort_bubble(array_cp))
print('\n')

array_cp = array[:]

print("Исходный массив")
print(array_cp)
print('\n')

print("Быстрая сортировка")
sort_quick_time_start = time.time()
sort_quick(array_cp)
sort_quick_time_end = time.time()
sort_quick_time = sort_quick_time_end - sort_quick_time_start
print("Время быстрой сортировки", sort_quick_time)
print(sort_quick(array_cp))


