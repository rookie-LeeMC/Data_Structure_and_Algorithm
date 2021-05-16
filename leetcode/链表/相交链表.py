# -*- coding:UTF-8 -*-
'''
编写一个程序，找到两个单链表相交的起始节点。


https://leetcode-cn.com/problems/intersection-of-two-linked-lists/solution/python3zhi-jie-fa-by-pandawakaka/
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 思路很简单，就是用数组存储起来，然后再逆序找，代码如下：
    def getIntersectionNode_v1(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA == None or headB == None:
            return None

        listA = []
        listB = []

        while headA:
            listA.append(headA)
            headA = headA.next

        while headB:
            listB.append(headB)
            headB = headB.next

        same = None
        for idx in range(1, 1 + min(len(listA), len(listB))):
            idx = -1 * idx

            if listA[idx] != listB[idx]:
                break

            if listA[idx] == listB[idx]:
                same = listA[idx]

        return same

    # 会超时
    def getIntersectionNode_v1(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA == None or headB == None:
            return None

        dictA = {}
        while headA:
            dictA[headA] = 1
            headA = headA.next

        while headB:
            if headB in dictA:
                return headB

        return None

    def getIntersectionNode_v1(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA == None or headB==None:
            return None

        ha = headA
        hb = headB

        while ha !=hb:
            ha = ha.next if ha else headB
            hb = hb.next if hb else headA

        return ha