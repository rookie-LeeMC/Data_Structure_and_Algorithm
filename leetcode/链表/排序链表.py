# -*- coding:UTF-8 -*-
'''
题目
https://leetcode-cn.com/problems/sort-list/solution/

解题
https://leetcode-cn.com/problems/sort-list/solution/sort-list-gui-bing-pai-xu-lian-biao-by-jyd/
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        ## 边界判定
        if head == None or head.next == None:
            return head

        ## 分割cut环节
        # 快慢指针法：奇数个节点找到中点，偶数个节点找到中心左边的节点
        slow = head
        fast = head.next

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        # 从中间切断链表
        mid = slow.next
        slow.next = None

        left = self.sortList(head)
        right = self.sortList(mid)

        ########## 递归终止

        ## 合并 merge 环节
        h = res = ListNode(0)

        while left != None and right != None:
            if left.val <= right.val:
                h.next = left
                left = left.next
                h = h.next
            else:
                h.next = right
                right = right.next
                h = h.next

        if left != None:
            h.next = left
        else:
            h.next = right

        return res.next


