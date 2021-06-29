# -*- coding:UTF-8 -*-
'''
https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/solution/dian-hua-hao-ma-de-zi-mu-zu-he-by-leetcode-solutio/
'''


def letterCombinations(digits):
    if not digits: return []

    phoneMap = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    ans = []
    comb = []

    def trackback(index):  # index为探索的新区域
        if index == len(digits):
            ans.append("".join(comb))
            return

        digit = digits[index]
        for letter in phoneMap[digit]:
            comb.append(letter)
            trackback(index + 1)
            comb.pop()

    trackback(0)
    return ans


digits = "23"
print(letterCombinations(digits))
