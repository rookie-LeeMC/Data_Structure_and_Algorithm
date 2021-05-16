# -*- coding:UTF-8 -*-
'''
https://leetcode-cn.com/problems/insert-interval/
'''


def insert(intervals, newInterval):
    intervals.append(newInterval)
    if len(intervals) < 2: return intervals

    intervals = sorted(intervals, key=lambda x: x[0])
    ans = []
    ans.append(intervals[0])

    for i in range(1, len(intervals)):
        if ans[-1][1] >= intervals[i][0] and ans[-1][1] >= intervals[i][1]:
            continue
        elif ans[-1][1] >= intervals[i][0] and ans[-1][1] < intervals[i][1]:
            ans[-1][1] = intervals[i][1]
        elif ans[-1][1] < intervals[i][0]:
            ans.append(intervals[i])

    return ans


intervals = [[1, 3], [6, 9]]
newInterval = [2, 5]
print(insert(intervals, newInterval))
