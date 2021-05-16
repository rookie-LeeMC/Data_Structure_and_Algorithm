# -*- coding:UTF-8 -*-
'''
https://leetcode-cn.com/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof/solution/mian-shi-ti-53-i-zai-pai-xu-shu-zu-zhong-cha-zha-5/

思考：二分法查找固定的数字、找指定数组的左右边界(通过判断条件)
看labuladong
'''


# 抽象一下，想象成找target在有序数组中插入的最右侧区间
def search(nums, target):
    if not nums or nums[-1] < target or nums[0] > target: return 0

    def helper(target):
        i, j = 0, len(nums) - 1
        while i <= j:
            mid = (i + j) // 2

            if nums[mid] < target:
                i = mid + 1
            elif nums[mid] > target:
                j = mid - 1
            else:
                i = mid + 1

        return i

    return helper(target) - helper(target - 1)


def left_bound(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:  # 左闭右闭区间，还有元素时就判断
        mid = left + (right - left) // 2
        if nums[mid] == target:
            right = mid - 1
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1

    return left,right

def right_bound(nums,target):
    left,right=0,len(nums)-1

    while left<=right:
        mid= left+(right-left)//2

        if nums[mid]==target:
            left=mid+1
        elif nums[mid]>target:
            right=mid-1
        elif nums[mid]<target:
            left=mid+1

    return left,right


print(search([5, 7, 7, 8, 8, 10], 8))
print(left_bound([5, 7, 7, 8, 8, 10], 8))
print(right_bound([5, 7, 7, 8, 8, 10], 8))
