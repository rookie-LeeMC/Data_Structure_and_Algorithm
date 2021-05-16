# -*- coding:UTF-8 -*-


'''
斐波那契数列
'''


def palouti(n):
    if n <= 2:
        return n

    ans = [0 for i in range(n + 1)]
    ans[1] = 1
    ans[2] = 2

    for i in range(3, n + 1):
        ans[i] = ans[i - 1] + ans[i - 2]

    return ans[n]


ans = palouti(4)
print(ans)
