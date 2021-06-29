# -*- coding:UTF-8 -*-
'''
226. 翻转二叉树
翻转一棵二叉树。

使用递归方式
1、递归边界
若翻转时节点为空，则停止

2、一般情况
左子树和右子树进行交换，交换后左子树、右子树分别调用 函数自己 进行构建
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root