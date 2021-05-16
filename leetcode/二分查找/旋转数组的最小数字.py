# -*- coding:UTF-8 -*-
'''
https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/
'''


def minArray(numbers):
    if not numbers: return None
    if len(numbers) == 1: return numbers[0]

    start,end=0,len(numbers)-1
    while start<end:
        mid = (start+end)//2

        if numbers[mid]>numbers[end]:
            start=mid+1
        elif numbers[mid]<numbers[end]:
            end=mid
        elif numbers[mid]==numbers[end]:
            end-=1

    return numbers[start]
# print(minArray([3,4,5,1,2]))
# print(minArray([2,2,2,0,1]))
print(minArray([3, 1, 3]))
