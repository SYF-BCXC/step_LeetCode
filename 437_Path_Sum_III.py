#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 437_Path_Sum_III
# @Author  : TCY
# @Time    : 2019/5/9 12:19
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        """双递归。
        1. 递归出口
        2. 递归主体。同样利用把加法转为减法的思路。然后采取两种决策思路，当前节点选择或者不选择。
        """
        # Edge case
        if root == None:
            return 0

        # process
        def recur(node, target):
            if node == None:
                return 0

            res = 0
            if node.val == target:
                res += 1

            res = res + recur(node.left, target - node.val) + recur(node.right, target - node.val)
            return res

        # recursion
        return recur(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
