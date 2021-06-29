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


def sortList(head):
    if not head or not head.next: return head

    # 分割环节
    # 快慢指针法：奇数个节点找到中点，偶数个节点找到中心左边的节点
    slow = head
    fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # 切断链表
    mid = slow.next
    slow.next = None

    # 分左边
    left = sortList(head)
    # 分右边
    right = sortList(mid)

    # 治理合并
    h = res = ListNode(-1)
    while left and right:
        if left.val > right.val:
            h.next = right
            right = right.next
            h = h.next
        else:
            h.next = left
            left = left.next
            h = h.next

    if left:
        h.next = left
    elif right:
        h.next = right

    return res.next


def sortList_v1(head):
    if not head or not head.next: return head

    # 快慢指针法分割链表
    slow = head
    fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # 切断链表
    mid = slow.next
    slow.next = None

    # 分左边
    left = sortList_v1(head)
    # 分右边
    right = sortList_v1(mid)

    # 治理合并
    h = ans = ListNode(-1)
    while left and right:
        if left.val <= right.val:
            h.next = left
            h = h.next
            left = left.next
        elif left.val > right.val:
            h.next = right
            h = h.next
            right = right.next

    if left:
        h.next = left
    elif right:
        h.next = right

    return ans.next


def sortList_20210612(head):
    if not head or not head.next: return head

    # 快慢指针法，找到中间节点
    slow = head
    fast = head.next
    while fast.next:
        slow = slow.next
        fast = fast.next.next

    # 断开链表
    mid = slow.next
    slow.next = None

    # 分左、右 划分
    left = sortList_20210612(head)
    right = sortList_20210612(mid)

    # 治理合并、有序链表合并
    h = ans = ListNode(-1)
    while left and right:
        if left.val <= right.val:
            h.next = left
            h = h.next
            left = left.next
        else:
            h.next = right
            h = h.next
            right = right.next

    if left:
        h.next = left
    elif right:
        h.next = right

    return ans.next
