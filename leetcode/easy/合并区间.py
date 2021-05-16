# -*- coding:UTF-8 -*-
'''
https://leetcode-cn.com/problems/merge-intervals/description/?utm_source=LCUS&utm_medium=ip_redirect&utm_campaign=transfer2china
'''


def merge(intervals):
    if not intervals: return []
    if len(intervals) == 1: return intervals[0]

    intervals = sorted(intervals, key=lambda x: x[0])
    # print(intervals)
    ans = []
    ans.append(intervals[0])

    for i in range(1, len(intervals)):
        if ans[-1][1] >= intervals[i][0] and ans[-1][1] <= intervals[i][1]:
            ans[-1][1] = intervals[i][1]
        elif ans[-1][1] > intervals[i][1]:
            continue
        elif ans[-1][1] < intervals[i][0]:
            ans.append(intervals[i])

    return ans


print(merge([[1, 3], [2, 6], [15, 18], [8, 10]]))
