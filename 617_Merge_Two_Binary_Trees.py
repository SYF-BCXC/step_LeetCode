#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 617_Merge_Two_Binary_Trees
# @Author  : TCY
# @Time    : 2019/5/9 10:36
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 == None and t2 == None:
            return None
        if t1 == None:
            return t2
        if t2 == None:
            return t1
        m = TreeNode(t1.val + t2.val)
        m.left = self.mergeTrees(t1.left, t2.left)
        m.right = self.mergeTrees(t1.right, t2.right)
        return m
