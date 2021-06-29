# -*- coding:UTF-8 -*-

def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


# 二叉树的层序遍历:优先队列
def levelOrder(root):
    if not root: return []
    if not root.left and not root.right: return [[root.val]]

    ans = []
    stack = []
    stack.append(root)

    while stack:
        n = len(stack)
        level = []

        for i in range(n):
            node = stack.pop(0)
            level.append(node.val)

            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)
        ans.append(level)

    return ans


# 前序遍历
def preorderTraversal(root):
    # 递归
    # if not root: return []
    # if not root.left and not root.right: return [[root.val]]
    #
    # ans = []
    #
    # def pre_order(root):
    #     if not root: return
    #     ans.append(root.val)
    #     pre_order(root.left)
    #     pre_order(root.right)
    #
    # pre_order(root)
    #
    # return ans

    # 非递归
    if not root: return []
    if not root.left and not root.right: return [root.val]

    ans = []
    stack = []

    while stack or root:
        while root:
            ans.append(root.val)
            stack.append(root)
            root = root.left
        root = stack.pop()
        root = root.right

    return ans


# 中序遍历
def inorderTraversal(root):
    if not root: return []
    if not root.left and not root.right: return [root.val]

    ans = []
    stack = []

    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        ans.append(root.val)
        root = root.right

    return ans


# 后序遍历:左右根--根右左，然后反转
def postorderTraversal(root):
    if not root: return []
    if not root.left and not root.right: return [root.val]

    ans = []
    stack = []
    while stack or root:
        while root:
            ans.append(root.val)
            stack.append(root)
            root = root.right
        root = stack.pop()
        root = root.left

    return ans[::-1]

# 剑指 Offer 33. 二叉搜索树的后序遍历序列

