# -*- coding:UTF-8 -*-
'''
https://leetcode-cn.com/problems/he-bing-liang-ge-pai-xu-de-lian-biao-lcof/
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def mergeTwoLists(l1, l2):
    if not l1: return l2
    if not l2: return l1

    tmp = ListNode(0)
    ans = tmp

    # 交替取值

    while l1 and l2:
        if l1.val<=l2.val:
            tmp.next = ListNode(l1.val)
            l1 = l1.next
        else:
            tmp.next = ListNode(l2.val)
            l2 = l2.next

        tmp = tmp.next

    if not l1:
        tmp.next = l2
    if not l2:
        tmp.next = l1

    return ans.next




