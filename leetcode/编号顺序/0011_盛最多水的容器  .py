# -*- coding:UTF-8 -*-
'''
解题：双指针法
https://leetcode-cn.com/problems/container-with-most-water/solution/sheng-zui-duo-shui-de-rong-qi-by-leetcode-solution/
'''


def maxArea(height):
    if len(height) < 2: return 0

    ans = 0
    left, right = 0, len(height) - 1
    while left < right:
        area = min(height[left], height[right]) * (right - left)
        ans = max(ans, area)

        if height[left] <= height[right]:
            left += 1
        else:
            right -= 1

    return ans


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(maxArea(height))
