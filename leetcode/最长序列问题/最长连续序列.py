# -*- coding:UTF-8 -*-
'''
https://leetcode-cn.com/problems/longest-consecutive-sequence/solution/dong-tai-gui-hua-python-ti-jie-by-jalan/
'''


# 动态规划
def longestConsecutive(nums) -> int:
    res = 0
    hash_dict = dict()
    for num in nums:
        # 新进来哈希表一个数
        if num not in hash_dict:
            # 获取当前数的最左边连续长度,没有的话就更新为0
            left = hash_dict.get(num - 1, 0)
            # 同理获取右边的数
            right = hash_dict.get(num + 1, 0)
            """不用担心左边和右边没有的情况
            因为没有的话就是left或者right0
            并不改变什么
            """
            # 把当前数加入哈希表，代表当前数字出现过
            hash_dict[num] = 1
            # 更新长度
            length = left + 1 + right
            res = max(res, length)
            # 更新最左端点的值，如果left=n存在，那么证明当前数的前n个都存在哈希表中
            hash_dict[num - left] = length
            # 更新最右端点的值，如果right=n存在，那么证明当前数的后n个都存在哈希表中
            hash_dict[num + right] = length
            # 此时 【num-left，num-right】范围的值都连续存在哈希表中了
            # 即使left或者right=0都不影响结果
    return res


# hash表-贪心
def longestConsecutive_v2(nums):
    res = 0
    nums_set = set(nums)

    for num in nums_set:
        if num - 1 not in nums_set:

            num_cur = num
            num_len = 1

            while num_cur + 1 in nums_set:
                num_cur += 1
                num_len += 1

            res = max(res, num_len)

    return res


print(longestConsecutive([4, 3]))
print(longestConsecutive_v2([4, 3]))
