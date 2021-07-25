# -*- coding:UTF-8 -*-
class Solution:
    def trap(self, height) -> int:
        ans = 0
        left, right = 0, len(height) - 1
        leftMax = rightMax = 0

        while left < right:
            leftMax = max(leftMax, height[left])
            rightMax = max(rightMax, height[right])
            if height[left] < height[right]:
                ans += leftMax - height[left]
                left += 1
            else:
                ans += rightMax - height[right]
                right -= 1

        return ans


#
# 输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出：6


a = {5: 5, 4: 4, 8: 8}
print(sorted(a.items(), key=lambda x: (x[1], x[0])))
