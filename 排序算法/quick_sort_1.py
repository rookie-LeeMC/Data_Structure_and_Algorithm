# -*- coding: UTF-8 -*-
'''
此方法为左右指针法，交换为同步交换

步骤详解
https://blog.csdn.net/qq_36528114/article/details/78667034
'''


def swap(data, idx1, idx2):
    data[idx1], data[idx2] = data[idx2], data[idx1]


def partition(data, left, right):
    base_idx = left
    base = data[left]

    while left < right:
        while left < right and data[left] <= base:
            left += 1

        while left < right and data[right] >= base:
            right -= 1

        # 同步交换
        swap(data, left, right)

    if data[left] < base and left == right:
        swap(data, base_idx, left)

    return left


def quick_sort_1(data, left, right):
    if left < right:
        mid = partition(data, left, right)
        # print(data)
        quick_sort_1(data, left, mid - 1)
        quick_sort_1(data, mid, right)


a = [2, 4, 5, 1, 3]
# print(a)
quick_sort_1(a, 0, len(a) - 1)
print(a)