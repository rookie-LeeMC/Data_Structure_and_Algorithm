# -*- coding:UTF-8 -*-
'''
题目
https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/

解题：双指针法
https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/solution/shan-chu-lian-biao-de-dao-shu-di-nge-jie-dian-b-61/
'''


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def removeNthFromEnd_20210613(self, head: ListNode, n: int) -> ListNode:
    '''
        哑结点 + 快慢指针法
    '''
    if not head or not head.next: return None

    dummy = ListNode(-1)  # 哑结点
    dummy.next = head
    first = head
    second = dummy

    for _ in range(n):
        first = first.next

    while first:
        first = first.next
        second = second.next

    second.next = second.next.next

    return dummy.next


def removeNthFromEnd_20210627(self, head: ListNode, n: int) -> ListNode:
    if not head: return head

    dummy = ListNode(-1)
    dummy.next = head
    first = head
    second = dummy

    for _ in range(n):
        first = first.next

    while first:
        first = first.next
        second = second.next

    second.next = second.next.next

    return dummy.next
