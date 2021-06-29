# -*- coding:UTF-8 -*-
'''
https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii/
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteDuplicates(head):
    if not head or not head.next: return head

    dummy = ListNode(-1)
    dummy.next = head
    cur = dummy

    while cur.next and cur.next.next:
        if cur.next.val == cur.next.next.val:
            x = cur.next.val
            while cur.next and cur.next.val == x:
                cur.next = cur.next.next
        else:
            cur = cur.next

    return dummy.next
