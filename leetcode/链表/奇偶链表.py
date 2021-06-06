# -*- coding:UTF-8 -*-
'''
解题
https://leetcode-cn.com/problems/odd-even-linked-list/solution/qi-ou-lian-biao-by-leetcode-solution/
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def oddEvenList(head):
    if not head or not head.next or not head.next.next: return head

    # 备份奇链表、偶链表的头结点
    ans = head
    even_head = head.next

    odd = head
    even = head.next

    while even and even.next:
        odd.next = even.next  # 指向下一个奇节点
        odd = odd.next
        even.next = odd.next  # 指向下一个偶节点
        even = even.next

    odd.next = even_head

    return head


head = tmp = ListNode(1)
tmp.next = ListNode(2)
tmp = tmp.next
tmp.next = ListNode(3)
tmp = tmp.next
tmp.next = ListNode(4)
tmp = tmp.next
tmp.next = ListNode(5)
tmp = tmp.next

h = oddEvenList(head)
a = 1
