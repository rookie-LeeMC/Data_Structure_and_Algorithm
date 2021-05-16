# -*- coding:UTF-8 -*-
'''
234. 回文链表

请判断一个链表是否为回文链表。

示例 1:

输入: 1->2
输出: false

示例 2:

输入: 1->2->2->1
输出: true
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        val_list = []
        while head:
            val_list.append(head.val)
            head = head.next

        return val_list == val_list[::-1]
