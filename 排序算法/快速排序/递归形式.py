# -*- coding-8 -*-
'''
参考资料
https://zhuanlan.zhihu.com/p/109810205
'''

def partition(nums, left, right):
    '''
    切分函数：找到切分点位置，并做好切分点左右排布
    异步交换方式
    '''

    base = nums[left]

    while left < right:
        while left < right and nums[right] >= base:
            right -= 1
        nums[left] = nums[right]

        while left < right and nums[left] <= base:
            left += 1
        nums[right] = nums[left]

    nums[left] = base

    return left


def quick_sort(nums, left, right):
    if left < right:
        mid = partition(nums, left, right)
        quick_sort(nums, left, mid - 1)
        quick_sort(nums, mid + 1, right)


a = [2, 4, 5, 1, 3]
print(a)
quick_sort(a, 0, len(a) - 1)
print(a)
