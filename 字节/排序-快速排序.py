# -*- coding:UTF-8 -*-

def partition(data, left, right):
    # 异步交换
    base = data[left]

    while left < right:
        while left < right and data[right] > base: right -= 1
        data[left] = data[right]
        while left < right and data[left] <= base: left += 1
        data[right] = data[left]
    data[left] = base
    return left


def partitions_v2(arr, left, right):
    # 同步交换
    i, j = left, right

    while i < j:
        while i < j and arr[j] >= arr[left]: j -= 1
        while i < j and arr[i] <= arr[left]: i += 1

        arr[i], arr[j] = arr[j], arr[i]
    arr[left], arr[i] = arr[i], arr[left]

    return i


def quick_sort(data, left, right):
    if left < right:
        mid = partitions_v2(data, left, right)
        quick_sort(data, left, mid - 1)
        quick_sort(data, mid + 1, right)


a = [2, 4, 5, 1, 3]
print(a)
quick_sort(a, 0, len(a) - 1)
print(a)
