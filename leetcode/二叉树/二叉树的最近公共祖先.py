# -*- coding:UTF-8 -*-
'''
https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/
'''


def lowestCommonAncestor(root, p, q):
    if not root: return None

    def common_node(root, p, q):
        if not root or root == p or root == q: return root

        left=common_node(root.left,p,q)
        right=common_node(root.right,p,q)

        if not left:
            return right
        if not right:
            return left

        return root

    return common_node(root,p,q)
