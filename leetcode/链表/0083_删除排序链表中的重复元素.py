# -*- coding:UTF-8 -*-
'''
https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteDuplicates(head):
    if not head or not head.next: return head

    cur = head
    while cur.next:
        if cur.val == cur.next.val:
            cur.next = cur.next.next
        else:
            cur = cur.next

    return head


head = tmp = ListNode(1)
tmp.next = ListNode(1)
tmp = tmp.next
tmp.next = ListNode(2)
tmp = tmp.next
tmp.next = ListNode(3)
tmp = tmp.next
tmp.next = ListNode(3)
tmp = tmp.next

print(deleteDuplicates(head))
