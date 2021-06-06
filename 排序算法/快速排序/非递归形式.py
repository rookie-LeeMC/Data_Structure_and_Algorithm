# -*- coding-8 -*-

class Stack():
    """简单实现一个栈，本质就是个list"""

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


def partition(nums, left, right):
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


def quick_sort(nums):
    stack = Stack()
    start, end = 0, len(nums) - 1

    # 进行第一层判断
    if start < end:
        stack.push((start, end))

        while not stack.is_empty():
            start, end = stack.pop()
            mid = partition(nums, start, end)

            # 保证mid左侧数量大于一个，这样才有排序的必要
            if start < mid - 1:
                stack.push((start, mid - 1))

            # 保证mid右侧数量大于一个，这样才有排序的必要
            if end > mid + 1:
                stack.push((mid + 1, end))


a = [2, 4, 5, 1, 3]
print(a)
quick_sort(a)
print(a)
