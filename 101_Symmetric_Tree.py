#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 101_Symmetric_Tree
# @Author  : TCY
# @Time    : 2019/5/10 11:01
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        """递归比较两棵树"""

        def helper(a, b):
            # edge case
            if not a and not b:
                return True
            if not a or not b:
                return False

            # process
            flag = (a.val == b.val)

            # recursion
            return helper(a.left, b.right) and helper(a.right, b.left) if flag else flag

        if root == None:
            return True
        return helper(root.left, root.right)