# -*- coding:UTF-8 -*-
'''
https://leetcode-cn.com/problems/rotate-list/
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def gen_len(head):
    n = 1
    cur = head
    while cur.next:
        cur = cur.next
        n += 1
    return n


def rotateRight(head, k):
    if k == 0 or not head or not head.next: return head

    # 求链表长度，并获取尾部节点
    n = 1
    cur = head
    while cur.next:
        cur = cur.next
        n += 1

    k1 = k % n
    if k1 == 0: return head

    cur.next = head
    k2 = n - k1
    while k2 > 0:
        head = head.next
        cur = cur.next
        k2 -= 1

    cur.next=None

    return head


l = ListNode(0)
d = l
l.next = ListNode(1)
l = l.next
l.next = ListNode(2)

print(rotateRight(d, 4).val)
