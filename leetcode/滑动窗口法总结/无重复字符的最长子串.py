# -*- coding:UTF-8 -*-
'''
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

 

示例 1:

输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/

解法：
滑动窗口 循序渐进的3个改进方法
https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/solution/python-hua-dong-chuang-kou-xun-xu-jian-jin-de-3ge-/
'''


class Solution:
    def lengthOfLongestSubstring(self, s):
        if len(s) == 0 or len(s) == 1: return len(s)

        max_len = 1
        for i in range(len(s) - 1):
            tmp = {}
            tmp[s[i]] = 0
            tmp_len = 1

            for j in range(i + 1, len(s)):
                if s[j] in tmp.keys():
                    break
                tmp_len += 1
                tmp[s[j]] = 0

            if tmp_len > max_len:
                max_len = tmp_len

        return max_len

    # 滑动窗--数组
    def lengthOfLongestSubstring_v1(self, s):
        n = len(s)
        if n == 0 or n == 1:    return n

        # 滑动窗口
        windows = []
        # 最大不重复子串长度
        max_len = 0

        for i in range(len(s)):
            # 字符 不在滑动窗内
            if s[i] not in windows:
                # 插入滑动窗
                windows.append(s[i])
            # 字符 在滑动窗内
            else:
                # 丢弃滑动窗内重复的字符
                windows = windows[windows.index(s[i]) + 1:]
                # 插入滑动窗
                windows.append(s[i])

            max_len = max(max_len, len(windows))

        return max_len

    # 滑动窗--双指针
    def lengthOfLongestSubstring_v2(self, s):
        n = len(s)
        if n == 0 or n == 1:    return n

        # 滑动窗口 指针
        left, right = 0, 0
        # 最大不重复子串长度
        max_len = 0

        for idx, val in enumerate(s):
            # 字符 不在滑动窗口内
            if val not in s[left:right]:
                # 拓展
                right += 1
            # 字符 在滑动窗口内
            else:
                # 去除重复：left移动到第一个重复元素右边
                left += s[left:right].index(val) + 1
                # 拓展
                right += 1

            max_len = max(max_len, right - left)

        return max_len

    def lengthOfLongestSubstring_v3(self, s):
        if len(s) <= 1: return len(s)
        left, right = 0, 0
        max_len = -1

        for idx, val in enumerate(s):
            if val not in s[left:right]:
                right += 1
            else:
                left += s[left:right].index(val) + 1
                right += 1

            max_len = max(max_len, right - left)

        return max_len


s = Solution()
print(s.lengthOfLongestSubstring_v3('abcabcbb'))
print(s.lengthOfLongestSubstring_v3('pwwkew'))

print('*' * 20)

print(s.lengthOfLongestSubstring_v2('abcabcbb'))
print(s.lengthOfLongestSubstring_v2('pwwkew'))
