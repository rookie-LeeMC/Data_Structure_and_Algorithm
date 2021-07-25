# -*- coding-8 -*-

# def partition(nums, left, right):
#     base = nums[left]
#
#     while left < right:
#         while left < right and nums[right] >= base:
#             right -= 1
#         nums[left] = nums[right]
#
#         while left < right and nums[left] <= base:
#             left += 1
#         nums[right] = nums[left]
#
#     nums[left] = base
#     return left
#
#
# # 递归形式
# def quick_sort(nums, left, right):
#     if left < right:
#         mid = partition(nums, left, right)
#         quick_sort(nums, left, mid - 1)
#         quick_sort(nums, mid + 1, right)
#
#
# # 非递归形式
# # 递归可以转换成：每个区间压入栈，然后在下一个循环中弹出
# def quick_sort_stack(nums):
#     if not nums or len(nums) == 1: return nums
#
#     left, right = 0, len(nums) - 1
#     stack = []
#     stack.append((left, right))
#
#     while stack:
#         left, right = stack.pop()
#         mid = partition(nums, left, right)
#
#         if left < mid - 1:
#             stack.append((left, mid - 1))
#         if mid + 1 < right:
#             stack.append((mid + 1, right))


# 切分函数:异步交换
def partitions(nums, left, right):
    base = nums[left]
    while left < right:
        while left < right and nums[right] > base:
            right -= 1
        nums[left] = nums[right]

        while left < right and nums[left] <= base:
            left += 1
        nums[right] = nums[left]

    nums[left] = base  # 每次异步交换，剩下左进位
    return left


def quick_sort(nums, left, right):
    if left < right:
        mid = partitions(nums, left, right)
        quick_sort(nums, left, mid - 1)
        quick_sort(nums, mid + 1, right)


def quick_sort_stack(nums):
    if len(nums) < 2: return nums
    stack = []
    left, right = 0, len(nums) - 1
    stack.append((left, right))

    while stack:
        left, right = stack.pop()
        mid = partitions(nums, left, right)

        if left < mid - 1:
            stack.append((left, mid - 1))  # 压入待处理的左区间
        if mid + 1 < right:
            stack.append((mid + 1, right))  # 压入待处理的右区间


nums = [3, 7, 8, 3, 5, 2, 4, 8, 6, 4, 2, 9, 7]
quick_sort(nums, 0, len(nums) - 1)
print(nums)

nums = [3, 7, 8, 3, 5, 2, 4, 8, 6, 4, 2, 9, 7]
quick_sort_stack(nums)
print(nums)


def partitions_yb(nums, left, right):
    # i, j = left, right
    #
    # while i < j:
    #     while i < j and nums[j] >= nums[left]: j -= 1
    #     while i < j and nums[i] <= nums[left]: i += 1
    #     nums[i], nums[j] = nums[j], nums[i]
    # nums[i], nums[left] = nums[left], nums[i]
    # return i

    base = nums[left]
    while left < right:
        while left < right and nums[right] >= base: right -= 1
        nums[left] = nums[right]
        while left < right and nums[left] <= base: left += 1
        nums[right] = nums[left]

    nums[left] = base
    return left


def quick_sort_yb(nums, left, right):
    if left < right:
        mid = partitions_yb(nums, left, right)
        quick_sort_yb(nums, left, mid - 1)
        quick_sort_yb(nums, mid + 1, right)


nums = [3, 7, 8, 3, 5, 2, 4, 8, 6, 4, 2, 9, 7]
quick_sort_yb(nums, 0, len(nums) - 1)
print(nums)
