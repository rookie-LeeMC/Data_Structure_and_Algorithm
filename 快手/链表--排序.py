# -*- coding:UTF-8 -*-
'''
https://leetcode-cn.com/problems/sort-list/solution/
'''


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def sortList(head):
    if not head or not head.next: return head

    # 快慢指针分割数组
    slow = head
    fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # 切割链表
    mid = slow.next
    slow.next = None

    # 分左边
    left = sorted(head)
    # 分右边
    right = sortList(mid)

    # 治理合并
    h = ans = ListNode(-1)
    while left and right:
        if left.val >= right:
            h.next = right
            right = right.next
            h = h.next
        else:
            h.next = left
            left = left.next
            h = h.next

    if left:
        h.next = left
    elif right:
        h.next = right

    return ans.next
