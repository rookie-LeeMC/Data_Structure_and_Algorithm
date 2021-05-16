# -*- coding:UTF-8 -*-
'''
硬币找零问题总结
https://blog.csdn.net/Dby_freedom/article/details/102144772
'''
def func_2(coins, m):
    f = [float('inf')] * (m + 1)
    f[0] = 0
    for c in coins:  # 枚举硬币总数
        for j in range(m, c - 1, -1):  # 从大到小枚举金额，确保j-c >= 0.
            # print(j)
            f[j] = min(f[j], f[j - c] + 1)
            print(f)
    return f[m] if f[m] != float('inf') else -1  # 如果为inf说明状态不可达，返回-1即可。


coins = [1, 1, 2, 3]
m = 5
print(func_2(coins, m))
