# -*- coding:UTF-8 -*-
'''
https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/
'''


def minArray(numbers):
    if not numbers: return None
    if len(numbers) == 1: return numbers[0]

    start, end = 0, len(numbers) - 1
    while start < end:
        mid = (start + end) // 2

        if numbers[mid] > numbers[end]:
            start = mid + 1
        elif numbers[mid] < numbers[end]:
            end = mid
        elif numbers[mid] == numbers[end]:
            end -= 1

    return numbers[start]

# 错误
def minArray2(numbers):
    if not numbers: return None
    if len(numbers) == 1: return numbers[0]

    start, end = 0, len(numbers) - 1
    while start < end:
        mid = start + (end - start) // 2

        if numbers[mid] > numbers[start]:
            start = mid + 1
        elif numbers[mid] < numbers[start]:
            end = mid
        elif numbers[mid] == numbers[start]:
            start += 1   # 错误原因：当start和end相邻时，mid=start，且[start]==[end]，此时会跨过去mid，假如此刻mid是最小点，就会被跨过去

    return numbers[start]


print(minArray([3, 4, 5, 1, 2]))
print(minArray2([3, 4, 5, 1, 2]))
print(minArray([2, 2, 2, 0, 1]))
print(minArray2([2, 2, 2, 0, 1]))
# print(minArray([1, 3, 5]))
# print(minArray2([1, 3, 5]))
