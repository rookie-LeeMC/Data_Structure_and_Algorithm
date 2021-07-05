# -*- coding:UTF-8 -*-

'''
方法1：https://blog.csdn.net/qq_41765114/article/details/88415541
https://zhuanlan.zhihu.com/p/143558992
一、定义状态
dp[i]表示以a[i]结尾的最长递增子序列的长度

二、初始化定义

三、状态递归
dp[i] = max(dp[j])+1   dp[i]>dp[j]
else:   dp[i]=1

四、返回最大值
'''


# 动态规划
def lengthOfLIS(nums):
    n = len(nums)
    if n == 0 or n == 1: return n

    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            # 当前的和之前的逐个比较
            # print i,j
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


def lengthOfLIS(nums) -> int:
    size = len(nums)
    # 特判
    if size < 2:
        return size

    # 为了防止后序逻辑发生数组索引越界，先把第 1 个数放进去
    tail = [nums[0]]
    for i in range(1, size):
        # 【逻辑 1】比 tail 数组实际有效的末尾的那个元素还大
        # 先尝试是否可以接在末尾
        if nums[i] > tail[-1]:
            tail.append(nums[i])
            continue

        # 使用二分查找法，在有序数组 tail 中
        # 找到第 1 个大于等于 nums[i] 的元素，尝试让那个元素更小
        left = 0
        right = len(tail) - 1
        while left < right:
            # 选左中位数不是偶然，而是有原因的，原因请见 LeetCode 第 35 题题解
            mid = left + (right - left) // 2
            # mid = (left + right) >> 1
            if tail[mid] < nums[i]:
                # 中位数肯定不是要找的数，把它写在分支的前面
                left = mid + 1
            else:
                right = mid
        # 走到这里是因为【逻辑 1】的反面，因此一定能找到第 1 个大于等于 nums[i] 的元素，因此无需再单独判断
        tail[left] = nums[i]
    return len(tail)


nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(lengthOfLIS(nums))
print(lengthOfLIS([7, 7, 7, 7, 7, 7, 7]))
print(lengthOfLIS_v2(nums))
print(lengthOfLIS_v2([7, 7, 7, 7, 7, 7, 7]))
