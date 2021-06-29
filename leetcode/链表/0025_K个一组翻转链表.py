# -*- coding:UTF-8 -*-
'''
题目
https://leetcode-cn.com/problems/reverse-nodes-in-k-group/solution/k-ge-yi-zu-fan-zhuan-lian-biao-by-leetcode-solutio/
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseKGroup(head, k):
    if not head or not head.next: return head

    def reverse(head, tail):
        pre = None
        cur = head

        while cur:
            cur_next = cur.next
            cur.next = pre

            pre = cur
            cur = cur_next

    hair = ListNode(-1)
    hair.next = head
    pre = hair

    while head:
        tail = pre
        # 查看剩余部分长度是否大于等于K
        for i in range(k):
            tail = tail.next
            if not tail:
                return hair.next

        nex = tail.next

        # 断开
        tail.next = None
        pre.next = None

        # 反转
        reverse(head, tail)

        pre.next = tail
        head.next = nex

        pre = head
        head = head.next

    return hair.next
