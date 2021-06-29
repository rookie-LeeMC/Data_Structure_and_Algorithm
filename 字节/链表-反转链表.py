# -*- coding:UTF-8 -*-
'''
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def reverseList(head):
    '''
    哑结点+双指针交换
    '''
    if not head or not head.next: return head

    pre = None
    cur = head

    while cur:
        cur_next = cur.next  # 存储下一个节点，防止丢失
        cur.next = pre

        pre = cur
        cur = cur_next

    return pre
