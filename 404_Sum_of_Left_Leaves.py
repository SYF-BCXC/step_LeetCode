#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 404_Sum_of_Left_Leaves
# @Author  : TCY
# @Time    : 2019/5/10 11:25
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def helper(r, flag):
            # r:TreeNode ; flag:is it a left node
            # edge case
            if not r:
                return 0
            if not r.left and not r.right and flag:
                return r.val

            # process
            lt, rt = helper(r.left, True), helper(r.right, False)

            # recursion
            return lt + rt

        return helper(root, False)