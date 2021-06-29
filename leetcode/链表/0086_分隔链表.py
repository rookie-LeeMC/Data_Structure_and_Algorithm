# -*- coding:UTF-8 -*-
'''
https://leetcode-cn.com/problems/partition-list/
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def partition(head, x):
    if not head: return head

    # 小于分成一堆，大于或等于分成一堆
    small = s = ListNode(-1)
    large = l = ListNode(-1)

    while head:
        # 判断加到哪个链表后面
        if head.val < x:
            s.next = head
            s = s.next
        elif head.val >= x:
            l.next = head
            l = l.next

        head = head.next

    l.next = None
    s.next = large.next

    return small.next
