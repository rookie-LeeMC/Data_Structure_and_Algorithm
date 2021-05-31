# -*- coding:UTF-8 -*-
'''
https://leetcode-cn.com/problems/3sum-closest/

解题思路：第一个指针从前往后遍历，另外两个指针在第一个指针设定的范围内对撞查找
'''


def threeSumClosest(nums, target):
    if len(nums) == 3: return sum(nums)

    n = len(nums)
    nums.sort()
    min_diff = float('inf')
    ans = float('inf')

    for i in range(0, n - 2):
        # 第一个指针处理
        if sum(nums[i:i + 3]) == target:
            return target

        l = i + 1
        r = n - 1

        while l < r:
            if (nums[i] + nums[l] + nums[r]) == target:
                return target
            # elif (nums[i] + nums[l] + nums[r]) > target:
            #     if abs(nums[i] + nums[l] + nums[r] - target) < min_diff:
            #         min_diff = abs(nums[i] + nums[l] + nums[r] - target)
            #         ans = nums[i] + nums[l] + nums[r]
            #     r -= 1
            # elif (nums[i] + nums[l] + nums[r]) < target:
            #     if abs(nums[i] + nums[l] + nums[r] - target) < min_diff:
            #         min_diff = abs(nums[i] + nums[l] + nums[r] - target)
            #         ans = nums[i] + nums[l] + nums[r]
            #     l += 1

            if abs(nums[i] + nums[l] + nums[r] - target) < min_diff:
                min_diff = abs(nums[i] + nums[l] + nums[r] - target)
                ans = nums[i] + nums[l] + nums[r]

            # 确定如何移动范围指针
            if nums[i] + nums[l] + nums[r] > target:
                r -= 1
            elif nums[i] + nums[l] + nums[r] < target:
                l += 1
    return ans


nums = [-1, 2, 1, -4]
target = 1
print(threeSumClosest(nums, target))


