# -*- coding:UTF-8 -*-
'''
https://zhuanlan.zhihu.com/p/105624690
'''

'''
归并：有2个有序表，合并成一个有序表的过程
'''


# def merge(li, low, mid, high):
#     i = low
#     j = mid + 1
#
#     ltmp = []
#     while i <= mid and j <= high:  # 只要左右两边都有数
#         if li[i] < li[j]:
#             ltmp.append(li[i])
#             i += 1
#         elif li[i] >= li[j]:
#             ltmp.append(li[j])
#             j += 1
#
#     # while执行完，肯定有一部分没有数
#     # 左边有数
#     while i <= mid:
#         ltmp.append(li[i])
#         i += 1
#     # 右边有数
#     while j <= high:
#         ltmp.append(li[j])
#         j += 1
#
#     li[low:high + 1] = ltmp


def merge_sort(li, low, high):
    if low < high:  # 至少有2个元素

        mid = (low + high) // 2
        # 归并排序左边
        merge_sort(li, low, mid)
        # 归并排序右边
        merge_sort(li, mid + 1, high)

        # 左右合并
        merge(li, low, mid, high)


def merge(li, low, mid, high):
    '''
    有序数组的归并：6,7,8,9,1,2,3,4
                  l     m       h
    '''
    i, j = low, mid + 1
    ltmp = []
    while i <= mid and j <= high:
        if li[i] >= li[j]:
            ltmp.append(li[j])
            j += 1
        elif li[i] < li[j]:
            ltmp.append(li[i])
            i += 1

    while i <= mid:
        ltmp.append(li[i])
        i += 1

    while j <= high:
        ltmp.append(li[j])
        j += 1

    li[low:high + 1] = ltmp


a = [2, 4, 5, 1, 3]
print(a)
merge_sort(a, 0, len(a) - 1)
print(a)
