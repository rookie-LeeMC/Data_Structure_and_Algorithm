# -*- coding:UTF-8 -*-
'''
https://leetcode-cn.com/problems/binary-tree-preorder-traversal/

详解：
https://blog.csdn.net/lq_lq314/article/details/79176953?utm_term=python%E4%BA%8C%E5%8F%89%E6%A0%91%E9%81%8D%E5%8E%86%E9%80%92%E5%BD%92%E9%9D%9E%E9%80%92%E5%BD%92&utm_medium=distribute.pc_aggpage_search_result.none-task-blog-2~all~sobaiduweb~default-0-79176953&spm=3001.4430
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 前序遍历递归
def preorderTraversal(root):
    if not root: return []

    ans = []

    def pre_order(root):
        if not root: return
        ans.append(root.val)
        pre_order(root.left)
        pre_order(root.right)

    pre_order(root)

    return ans


# 前序遍历非递归：根-左-右
def preorderTraversal_stack(root):
    if not root: return []

    stack = []
    ans = []

    while stack or root:
        while root:
            ans.append(root.val)
            stack.append(root)
            root = root.left
        root = stack.pop()
        root = root.right

    return ans


# 中序遍历递归
def inorderTraversal(root):
    if not root: return []

    ans = []

    def in_order(root):
        if not root: return
        in_order(root.left)
        ans.append(root.val)
        in_order(root.right)

    in_order(root)
    return ans


# 中序遍历非递归：左-跟-有
def inorderTraversal_stack(root):
    if not root: return []

    stack = []
    ans = []

    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        ans.append(root.val)
        root = root.right

    return ans


# 后序遍历递归
def postorderTraversal(root):
    if not root: return []

    ans = []

    def post_order(root):
        if not root: return
        post_order(root.left)
        post_order(root.right)
        ans.append(root.val)

    post_order(root)
    return ans


# 后序遍历非递归：左-右-根 --> 根-右-左 再翻转
def postorderTraversal_stack(root):
    if not root: return []

    stack = []
    ans = []

    while stack or root:
        while root:
            ans.append(root.val)
            stack.append(root)
            root = root.right
        root = stack.pop()
        root = root.left

    return ans[::-1]
