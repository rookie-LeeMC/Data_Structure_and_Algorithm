# -*- coding:UTF-8 -*-
'''
https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/
'''


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def flatten(root: TreeNode):
    if not root: return

    node_list = []

    def pre_order(root):
        if not root: return
        node_list.append(root)
        pre_order(root.left)
        pre_order(root.right)

    pre_order(root)

    head = node_list[0]
    head.left = None

    for i in range(1, len(node_list)):
        head.right = node_list[i]
        head = head.right
        head.left = None
