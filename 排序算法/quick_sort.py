# -*- coding: UTF-8 -*-
'''
此方法为挖坑法，交换为异步交换

步骤详解
https://blog.csdn.net/Dby_freedom/article/details/87966452

代码详解
https://www.cnblogs.com/Yanjy-OnlyOne/p/12411683.html
'''


def partition(data, left, right):
    base = data[left]  # 设置base：left指针位置是base

    while left < right:  # 指针不要交叉
        while left < right and data[right] >= base:  # 右指针左移动：找出小于base的位置
            right -= 1
        data[left] = data[right]

        while left < right and data[left] <= base:
            left += 1
        data[right] = data[left]

    data[left] = base

    return left


def quick_sort(data, left, right):
    if left < right:  # 判断指针是否交叉
        mid = partition(data, left, right)  # 走一趟，分成左小、右大两部分
        quick_sort(data, left, mid - 1)  # 快排左小部分
        quick_sort(data, mid + 1, right)  # 快排右大部分


a = [2, 4, 5, 1, 3]
print(a)
quick_sort(a, 0, len(a) - 1)
print(a)
