# -*- coding: UTF-8 -*-
'''
选择排序

步骤详解
https://blog.csdn.net/Dby_freedom/article/details/87967821
step1:从待排序数组中，找到关键字最小的元素
step2:如果做小的元素不是数组的第一个元素，将其和第一个元素互换
step3：从余下N-1个元素中，找出关键字最小的元素，重复1、2步，直到排序结束
'''


def selectsort(data):
    if len(data) == 0 or len(data) == 1:
        pass

    n = len(data)
    for i in range(0, n - 1):
        cur_idx = i
        min_idx = i

        for j in range(i + 1, n):
            if data[j] < data[min_idx]:
                min_idx = j

        data[cur_idx], data[min_idx] = data[min_idx], data[cur_idx]


a = [2, 4, 5, 1, 3, 10, 46, 2, 6, 8, 12, 34]
# print(a)
selectsort(a)
print(a)
