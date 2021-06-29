# -*- coding:UTF-8 -*-
'''
102. 二叉树的层序遍历

给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。



示例：
二叉树：[3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]

'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode):
        if root == None: return []

        res = []
        ans = []
        res.append(root.val)

        while len(res) != 0:
            node = res.pop(0)
            if node.left != None: res.append(node.left)
            if node.right != None: res.append(node.right)

            ans.append(node.val)

        return ans
