# -*- coding:UTF-8 -*-
'''
https://leetcode-cn.com/problems/binary-tree-level-order-traversal/
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode):
        if root == None:
            return []

        ans = []
        res = []
        res.append(root)

        while len(res)!=0:
            res_len = len(res)
            tmp = []

            for i in range(res_len):
                node = res.pop(0)
                tmp.append(node.val)

                if node.left !=None:
                    res.append(node.left)
                if node.right!=None:
                    res.append(node.right)

            ans.append(tmp)

        return ans