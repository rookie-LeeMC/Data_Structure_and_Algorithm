# -*- coding:UTF-8 -*-
'''
543. 二叉树的直径

给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。

示例 :
给定二叉树

          1
         / \
        2   3
       / \
      4   5

返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。
'''

'''
递归思路
1、递归边界
2、递归表达式：表达一般的情况
3、依据表达式，在中段循环调用自身
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    redis = 0

    def depth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        L = self.depth(root.left)
        R = self.depth(root.right)

        self.redis = max(self.redis, L + R)

        return max(L, R) + 1

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0

        self.depth(root)

        return self.redis
