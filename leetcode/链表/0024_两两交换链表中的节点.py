# -*- coding:UTF-8 -*-
'''
https://blog.csdn.net/qq_41231926/article/details/82377317

解题：三指针移动
https://blog.csdn.net/qq_41231926/article/details/82377317

刷题要提速
1、审题
2、自己想思路
3、查看思路，捋顺思路
4、代码，看不懂，先模仿
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swapPairs(head):
    if not head or not head.next: return head

    dummy = ListNode(-1)
    dummy.next = head
    temp = dummy

    while temp.next and temp.next.next:
        node1 = temp.next
        node2 = temp.next.next

        temp.next = node2
        node1.next = node2.next
        node2.next = node1
        temp = node1

    return dummy.next


def swapPairs2(head):
    if not head or not head.next: return head
    dummy = ListNode(-1)
    dummy.next = head
    temp = dummy

    while temp.next and temp.next.next:
        node1 = temp.next
        node2 = temp.next.next

        # 交换
        temp.next = node2
        node1.next = node2.next
        node2.next = node1

        temp = node1

    return dummy.next


def swapPairs_20210613(head):
    if not head or not head.next: return head
    dummy = ListNode(-1)
    dummy.next = head
    temp = dummy

    while temp.next and temp.next.next:
        node1 = temp.next
        node2 = temp.next.next

        temp.next = node2
        node1.next = node2.next
        node2.next = node1

        temp = node1

    return dummy.next


tmp = ListNode(1)
head = tmp

tmp.next = ListNode(2)
tmp = tmp.next

tmp.next = ListNode(3)
tmp = tmp.next

tmp.next = ListNode(4)
tmp = tmp.next

t = swapPairs(head)
