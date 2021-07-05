# -*- coding:UTF-8 -*-

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def zigzagLevelOrder(root):
    if not root: return []

    ans, stack = [], []
    stack.append(root)
    cnt = 1

    while stack:
        n = len(stack)
        tmp = []

        for i in range(n):
            node = stack.pop(0)
            tmp.append(node.val)

            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)

        if cnt % 2 == 1:
            ans.append(tmp)
        else:
            ans.append(tmp[::-1])
        cnt += 1
    return ans
