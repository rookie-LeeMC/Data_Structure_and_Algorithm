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


class Solution:
    '''
    双指针迭代
    我们可以申请两个指针，第一个指针叫 pre，最初是指向 null 的。
    第二个指针 cur 指向 head，然后不断遍历 cur。
    每次迭代到 cur，都将 cur 的 next 指向 pre，然后 pre 和 cur 前进一位。
    都迭代完了(cur 变成 null 了)，pre 就是最后一个节点了。
    动画演示如下：
    '''

    def reverseList(self, head: ListNode) -> ListNode:

        pre = None
        cur = head

        while cur:
            tmp = cur.next
            cur.next = pre

            pre = cur
            cur = tmp

        return pre

    def reverseList_1(self, head: ListNode) -> ListNode:
        '''
        解题思路：新建一个头结点，将所有的原链表节点从头到尾逐一取下，采用头插法插入整个链表到新建节点之前，则完成了链表逆序的目的。
        '''
        new_head = None

        while head:
            tmp = head.next

            head.next = new_head

            new_head = head
            head = tmp

        return new_head
