#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 112_Path_Sum
# @Author  : TCY
# @Time    : 2019/5/9 10:53
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        def recur(node, now, target):
            """递归.
            1. 边界情况判断。如果进来是空则返回False。
            2. now加上当前节点的值，如果当前节点是叶子节点，则返回True，不是叶子节点则递归。
            """
            if node == None:
                return False
            now += node.val
            if node.left == None and node.right == None:
                return now == target
            return recur(node.left, now, target) or recur(node.right, now, target)

        if root == None:
            return False
        return recur(root, 0, sum)
