# -*- coding:UTF-8 -*-
'''
题目
https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/

解题：双指针法
https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/solution/shan-chu-lian-biao-de-dao-shu-di-nge-jie-dian-b-61/
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    #     if head == None:
    #         return head
    #
    #     res = head
    #     cnt = 0
    #
    #     # 统计节点个数
    #     while head:
    #         cnt += 1
    #         head = head.next
    #
    #     delete = cnt + 1 - n
    #     pre = cnt - n
    #
    #     cnt = 0
    #     head = res
    #     # 关联节点与cnt，找到删除节点之前的node，调整即可
    #     while head:
    #         cnt += 1
    #         pre_node = head
    #         cur_node = head.next
    #         head = head.next
    #
    #         if cnt == pre:
    #             pre_node.next = cur_node.next
    #
    #     return res

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head == None or head.next == None:
            return None

        slow = ListNode(0)
        slow.next = head
        fast = slow

        for i in range(n):
            fast = fast.next

        while fast.next != None:
            slow = slow.next
            fast = fast.next

        if slow.next == head:
            return head.next
        else:
            slow.next = slow.next.next
            return head

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
