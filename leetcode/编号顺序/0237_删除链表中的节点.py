# -*- coding:UTF-8 -*-
'''
https://leetcode-cn.com/problems/delete-node-in-a-linked-list/
'''
# h
# 1>2>3>4>5

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def deleteNode(node):
    node.val = node.next.val
    node.next = node.next.next
