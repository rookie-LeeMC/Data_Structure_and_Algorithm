# -*- coding:UTF-8 -*-
'''

'''


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def reverse(head):
    if not head or (not head.next): return head

    pre = None
    cur = head

    while cur:
        cur_next = cur.next
        cur.next = pre

        pre = cur
        cur = cur_next

    return pre
