# -*- coding:UTF-8 -*-
'''
https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    min_dp = float('inf')

    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0

        def height(root):
            if not root.left and not root.right: return 1

            if root.left:
                self.min_dp = min(self.min_dp, height(root.left))
            if root.right:
                self.min_dp = min(self.min_dp, height(root.right))

            return 1 + self.min_dp

        return height(root)
