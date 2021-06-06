# -*- coding:UTF-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def detectCycle_dict(head):
    if not head or not head.next: return None
    if head.next == head: return head

    node_dic = {}
    while head:
        if head in node_dic.keys(): return head
        node_dic[head] = 1
        head = head.next

    return None
