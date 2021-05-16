# -*- coding:UTF-8 -*-
'''
给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数
https://leetcode-cn.com/problems/subarray-sum-equals-k/

题目类型
https://leetcode-cn.com/problems/subarray-sum-equals-k/solution/de-liao-yi-wen-jiang-qian-zhui-he-an-pai-yhyf/
'''


# 审题
# 思路
# pre[i]为0~i子数组之和，j~i子数组之和：pre[i]-pre[j-1] ，假如存在以i结尾的子数组之和为k，那pre[i]-k，必然存在于pre的数组中


# 代码

def subarraySum(nums, k):
    ans, tmp = 0, 0
    pre_dic = {0: 1}

    for i in range(len(nums)):
        tmp += nums[i]

        if tmp - k in pre_dic:
            ans += pre_dic[tmp - k]

        pre_dic[tmp] = pre_dic.get(tmp, 0) + 1

    return ans


nums = [1, 1, 1]
k = 2
print(subarraySum(nums, k))

nums = [-1, -1, 1]
k = 0
print(subarraySum(nums, k))
