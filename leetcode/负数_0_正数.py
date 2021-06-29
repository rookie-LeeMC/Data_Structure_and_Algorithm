# -*- coding:UTF-8 -*-


nums = [0, -1, -10, -1, 2, 2, -1, 0, 2]
# m = 0
# while nums[m] <= 0: m += 1
# nums[0], nums[m] = nums[m], nums[0]
# print(nums)


# for i in range(1,len(nums)):
#     if nums[m] == 0:
#         nums[m], nums[j + 1] = nums[j + 1], nums[m]
#         j += 1
#     elif nums[m] > 0:
#         nums[m], nums[i + 1] = nums[i + 1], nums[m]
#         i += 1
#         nums[m], nums[j + 1] = nums[j + 1], nums[m]
#         j += 1
# print(nums)

# 比较0和正数，负数自动插到前面

left = 0
right = len(nums) - 1

while left < right:
    while left < right and nums[left] <= 0:
        left += 1
    while left < right and nums[right] > 0:
        right -= 1

    nums[left], nums[right] = nums[right], nums[left]

print(left)
print(nums)
