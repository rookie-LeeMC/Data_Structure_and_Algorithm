# -*- coding: UTF-8 -*-
'''
选择排序

步骤详解
https://blog.csdn.net/Dby_freedom/article/details/87967009
按照关键字大小插入有序队列里
'''


def insertSort(data):
    if len(data) == 0 or len(data) == 1:
        pass

    n = len(data)
    for i in range(1, n):
        tmp = data[i]
        j = i - 1
        while j >= 0 and data[j] > tmp:
            data[j+1] = data[j]
            j -= 1

        data[j+1] = tmp


a=[6, 4, 8, 9, 2, 3, 1]
insertSort(a)
print(a)

