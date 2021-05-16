# -*- coding:UTF-8 -*-
'''
解题
https://leetcode-cn.com/problems/path-sum-iii/solution/437zhi-xu-yi-ci-di-gui-wu-xing-dai-ma-yong-lie-bia/

437. 路径总和 III

给定一个二叉树，它的每个结点都存放着一个整数值。

找出路径和等于给定数值的路径总数。

路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

二叉树不超过1000个节点，且节点数值范围是 [-1000000,1000000] 的整数。

示例：

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

返回 3。和等于 8 的路径有:

1.  5 -> 3
2.  5 -> 2 -> 1
3.  -3 -> 11
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


'''
双层递归
'''

# class Solution:
#     # 第一层递归
#     def pathSum(self, root, sum):
#         '''如果没有根节点，整个返回值应该为0，没有路径'''
#         if root == None:
#             return 0
#         '''
#         self.dfs(root, sum):判断当前节点出发是否有满足sum的path
#         self.pathSum(root.left, sum):判断从当前节点的左孩子出发是否有满足sum的path
#         self.pathSum(root.right, sum):判断从当前节点右孩子节点出发是否有满足sum的path
#         '''
#         return self.dfs(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
#
#     def dfs(self, root, path):
#         if root == None:
#             return 0
#
#         '''每一次都要减去当前层的节点值'''
#         path -= root.val
#
#         '''
#         (1 if path==0 else 0)：说明找到了路径
#         self.dfs(root.left, path) self.dfs(root.right, path)：
#           此时path更新过，这是因为当前点既可以往左走找path，也可以往右走，是或的关系，只要有一边找到了路径，最终结果都会为1
#         '''
#         return (1 if path == 0 else 0) + self.dfs(root.left, path) + self.dfs(root.right, path)


# class Solution:
#
#     def pathSum(self, root: TreeNode, sum: int) -> int:
#         def dfs(root, sumlist):
#             if root is None: return 0
#             sumlist = [val + root.val for val in sumlist] + [root.val]
#
#             return sumlist.count(sum) + dfs(root.left, sumlist) + dfs(root.right, sumlist)
#
#         return dfs(root, [])
#



l = [0, 1, 2, 3, 4]
print(id(l))
l.append(111)
print(id(l))

l = [num+2 for num in l]
print(id(l))

