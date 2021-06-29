# -*- coding:UTF-8 -*-
'''
https://leetcode-cn.com/problems/reverse-linked-list-ii/
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseBetween(head, left, right):
    if not head or left == right: return head

    def reverse_linked_list(head):
        '''
            反转单链表
        '''
        pre = None
        cur = head
        while cur:
            cur_next = cur.next
            cur.next = pre
            pre = cur
            cur = cur_next

    pre = dummy_node = ListNode(-1)
    dummy_node.next = head

    # 第 1 步：走到left之前的一个节点
    # 从虚拟头节点走 left - 1 步，来到 left 节点的前一个节点
    for _ in range(left - 1):
        pre = pre.next

    # 第 2 步：从 pre 再走 right - left + 1 步，来到 right 节点
    right_node = pre
    for _ in range(right - left + 1):
        right_node = right_node.next

    # 第 3 步：切断出一个子链表（截取链表）
    left_node = pre.next
    curr = right_node.next

    pre.next = None
    right_node.next = None

    # 子链表反转：左节点变为结尾，右节点变为开头
    reverse_linked_list(left_node)

    # 放回原来的表中
    pre.next = right_node
    left_node.next = curr

    return dummy_node.next
