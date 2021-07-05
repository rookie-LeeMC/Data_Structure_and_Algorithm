# -*- coding:UTF-8 -*-
'''
104. 二叉树的最大深度
给定一个二叉树，找出其最大深度。
二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。


使用递归方式
1、递归边界
若当前节点为空，则当前深度为0

2、一般情况
根节点提供了1个深度，然后加上左子树最大深度、右子树最大深度 的最大者
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
