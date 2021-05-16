# -*- coding:UTF-8 -*-
'''
https://leetcode-cn.com/problems/teemo-attacking/
'''


def findPoisonedDuration(timeSeries, duration):
    if duration == 0: return 0
    if not timeSeries: return 0
    if len(timeSeries) == 1: return duration

    ans = duration
    for i in range(1, len(timeSeries)):
        if timeSeries[i] - timeSeries[i - 1] < duration:
            ans += timeSeries[i] - timeSeries[i - 1]
        else:
            ans += duration

    return ans

print(findPoisonedDuration([1,2], 2))