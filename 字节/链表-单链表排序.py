# -*- coding:UTF-8 -*-
'''
https://leetcode-cn.com/problems/sort-list/solution/pai-xu-lian-biao-by-leetcode-solution/
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head

        def merge(head1, head2):
            dummy = ListNode(-1)
            h = dummy

            while head1 and head2:
                if head1.val >= head2.val:
                    h.next = head2
                    h = h.next
                    head2 = head2.next
                elif head1.val < head2.val:
                    h.next = head1
                    h = h.next
                    head1 = head1.next

            if head1:
                h.next = head1
            elif head2:
                h.next = head2

            return dummy.next

        ans = head
        slow, fast = head, head.next
        # 快慢指针，找到中间节点和尾部节点
        while fast and fast.next:  # fast为空，就不需要执行；fast.next为空，循环中就会报错
            slow = slow.next
            fast = fast.next.next

        # 断开链表
        mid = slow.next
        slow.next = None

        # 分左右分左右继续划分
        left = self.sortList(head)
        right = self.sortList(mid)

        # 合并左右有序链表
        ans = merge(left, right)

        return ans
