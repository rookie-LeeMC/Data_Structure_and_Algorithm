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

        while len(res) != 0:
            res_len = len(res)
            tmp = []

            for i in range(res_len):
                node = res.pop(0)
                tmp.append(node.val)

                if node.left != None:
                    res.append(node.left)
                if node.right != None:
                    res.append(node.right)

            ans.append(tmp)

        return ans




def level_order_list(root):
    if not root: return []

    ans = []
    nodes = []  # 优先队列
    nodes.append(root)

    while nodes:
        # 测量长度
        n = len(nodes)

        # 循环弹出，并压入非空的左右子树
        tmp = []
        for i in range(n):
            root = nodes.pop(0)
            tmp.append(root.val)

            if root.left:
                nodes.append(root.left)

            if root.right:
                nodes.append(root.right)

        ans.append(tmp)

    return ans


def level_order_v2(root):
    if not root: return []
    if not root.left and not root.right: return [[root.val]]

    ans = []
    stack = []
    stack.append(root)

    while stack:
        n = len(stack)
        tmp = []

        for i in range(n):
            node = stack.pop(0)
            tmp.append(node.val)

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        ans.append(tmp)

    return ans
