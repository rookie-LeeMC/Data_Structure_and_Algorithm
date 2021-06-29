'''
101. 对称二叉树
给定一个二叉树，检查它是否是镜像对称的。
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isMirror(root,root)

    def isMirror(self, p1, p2):
        if p1 is None and p2 is None:
            return True
        if (p1 is None and p2 is not None) or (p1 is not None and p2 is None):
            return False

        return p1.val == p2.val and self.isMirror(p1.left, p2.right) and self.isMirror(p1.right, p2.left)
