# -*- coding:UTF-8 -*-
'''
解题：深度优先+回溯法
https://leetcode-cn.com/problems/er-cha-shu-zhong-he-wei-mou-yi-zhi-de-lu-jing-lcof/
'''


class Solution:
    def pathSum(self, root, target):
        ret = list()
        path = list()

        def dfs(root, target):
            if not root:
                return
            path.append(root.val)
            target -= root.val
            if not root.left and not root.right and target == 0:
                ret.append(path[:])
            dfs(root.left, target)
            dfs(root.right, target)
            path.pop()

        dfs(root, target)
        return ret


def pathSum(root, target):
    ans = []
    path = []

    def dfs(root, target):
        if not root: return

        path.append(root.val)
        target -= root.val
        if not root.left and not root.right and target == 0:
            ans.append(path[:])

        dfs(root.left, target)
        dfs(root.right, target)

        path.pop()

    dfs(root, target)

    return ans
