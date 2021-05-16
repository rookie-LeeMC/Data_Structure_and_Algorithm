# -*- coding:UTF-8 -*-
'''
题目
https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/submissions/

解题
https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/solution/dong-hua-yan-shi-si-chong-jie-fa-114-er-cha-shu-zh/
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root):
        # 边界
        if root is None:
            return root

        node_list = []

        def pre_order(node):
            if node == None:
                return
            node_list.append(node)
            pre_order(node.left)
            pre_order(node.right)

        pre_order(root)

        head = node_list[0]
        head.left = None

        for i in range(1,len(node_list)):
            head.right = node_list[i]
            head = head.right
            head.left = None

