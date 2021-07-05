# -*- coding:UTF-8 -*-
'''
https://leetcode-cn.com/problems/single-number/
'''

def singleNumber(nums) -> int:
    if len(nums)==1:return nums[0]

    count={}
    for i in nums:
        count[i]=count.get(i,0)+1

    for i in count.keys():
        if count[i]==1:return i

print(singleNumber([2,2,1]))