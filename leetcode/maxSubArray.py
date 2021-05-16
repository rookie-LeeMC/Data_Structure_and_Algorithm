'''
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

进阶:

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
'''

a = [0, 1, 2, 3, 4, 5]
print(a[1:2])


def maxSubArray(nums):
    # if len(nums) == 1:
    #     return nums[0]
    #
    # max_sub_sum = nums[0]
    # for i in range(0, len(nums)):
    #     tmp = nums[i]
    #     max_sub_sum = tmp if tmp > max_sub_sum else max_sub_sum
    #
    #     for j in range(i + 1, len(nums)):
    #         tmp += nums[j]
    #
    #         max_sub_sum = tmp if tmp > max_sub_sum else max_sub_sum
    #
    # print(max_sub_sum)

    curr_sum, max_sum = nums[0], nums[0]

    for i in range(1,len(nums)):
        curr_sum = max(curr_sum+nums[i],nums[i])
        max_sum = max(max_sum,curr_sum)

    # print(max_sum)
    return max_sum



maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
maxSubArray([-2, 1])
