# -*- coding:UTF-8 -*-
'''
给你一个仅由大写英文字母组成的字符串，你可以将任意位置上的字符替换成另外的字符，总共可最多替换 k 次。在执行上述操作后，找到包含重复字母的最长子串的长度。

注意：字符串长度 和 k 不会超过 104。



示例 1：

输入：s = "ABAB", k = 2
输出：4
解释：用两个'A'替换为两个'B',反之亦然。

'''


def characterReplacement(s, k):
    if k == 0: return 0
    if len(s) == 0 or len(s) == 1: return len(s)

    length=len(s)
    left,right=0,0
    max_str_num=0
    str_list = [0]*26
    ans=0

    while right<length:
        str_list[ord(s[right])-ord('A')] +=1
        max_str_num=max(max_str_num,max(str_list))

        while (right-left+1-max_str_num)>k:
            # 更新状态

            str_list[ord(s[left])-ord('A')] -= 1
            left+=1

        ans = max(max_str_num,right-left+1)
        right+=1

    return ans
