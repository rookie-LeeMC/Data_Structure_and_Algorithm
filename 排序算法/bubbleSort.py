# -*- coding: UTF-8 -*-
'''
https://blog.csdn.net/Dby_freedom/article/details/87967779
https://blog.csdn.net/Dby_freedom/article/details/82154869
'''

'''
冒泡排序：
    重复走访要排序的数组，一次比较相邻的两个元素，不满足条件的进行交换，从而升序或者降序
'''


def bubble_sort(arry):
    n = len(arry)  # 获得数组的长度
    for i in range(n):
        for j in range(1, n - i):  # 每轮找到最大数值 或者用 for j in range(i+1, n)
            if arry[j - 1] > arry[j]:  # 如果前者比后者大
                arry[j - 1], arry[j] = arry[j], arry[j - 1]  # 则交换两者
    return arry


if __name__ == '__main__':
    l = [0, 5, 3, 7, 5, 8, 2]
    bubble = BubbleSort(l)
    print(bubble)
    bubble = BubbleSort(l, reverse=True)
    print(bubble)
