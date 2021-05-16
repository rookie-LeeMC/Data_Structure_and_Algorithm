# -*- coding:UTF-8 -*-
'''
参考解法
https://leetcode-cn.com/problems/longest-palindromic-substring/solution/zui-chang-hui-wen-zi-chuan-by-leetcode-solution/

class Solution {
    public String longestPalindrome(String s) {
        int len = s.length();
        // 特判
        if (len < 2){
            return s;
        }

        int maxLen = 1;
        int begin  = 0;

        // 1. 状态定义
        // dp[i][j] 表示s[i...j] 是否是回文串


        // 2. 初始化
        boolean[][] dp = new boolean[len][len];
        for (int i = 0; i < len; i++) {
            dp[i][i] = true;
        }

        char[] chars = s.toCharArray();
        // 3. 状态转移
        // 注意：先填左下角
        // 填表规则：先一列一列的填写，再一行一行的填，保证左下方的单元格先进行计算
        for (int j = 1;j < len;j++){
            for (int i = 0; i < j; i++) {
                // 头尾字符不相等，不是回文串
                if (chars[i] != chars[j]){
                    dp[i][j] = false;
                }else {
                    // 相等的情况下
                    // 考虑头尾去掉以后没有字符剩余，或者剩下一个字符的时候，肯定是回文串
                    if (j - i < 3){
                        dp[i][j] = true;
                    }else {
                        // 状态转移
                        dp[i][j] = dp[i + 1][j - 1];
                    }
                }

                // 只要dp[i][j] == true 成立，表示s[i...j] 是否是回文串
                // 此时更新记录回文长度和起始位置
                if (dp[i][j] && j - i + 1 > maxLen){
                    maxLen = j - i + 1;
                    begin = i;
                }
            }
        }
        // 4. 返回值
        return s.substring(begin,begin + maxLen);
    }
}
'''


def longestPalindrome(s):
    # 特殊情况
    if len(s) < 2: return s

    # 状态定义
    # dp[i][j]表示s[i,...,j]是否是回文子串

    # 初始化
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = True
    begin = 0
    maxlen = 1

    # 状态转移
    # 从左上角开始逐列填写
    for j in range(1, n):  # 对角线已经填写好
        for i in range(j):
            if s[i] != s[j]:
                dp[i][j] = False
            else:
                if j - 1 - (i + 1) + 1 < 2:  # 向内收收缩索引的边界，当只有一个数字，就是相遇时，不必判断，一定是回文
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i + 1][j - 1]

            if dp[i][j] and j - i + 1 > maxlen:
                maxlen = j - i + 1
                begin = i

    return s[begin:begin + maxlen]


print longestPalindrome("babad")
print longestPalindrome("cbbd")
print longestPalindrome("ac")
print longestPalindrome("aacabdkacaa")


8-14
17-24