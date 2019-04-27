#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 100_Same_Tree
# @Author  : TCY
# @Time    : 2019/4/27 12:42
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p, q):
        def dg(p, q):
            """递归判断"""
            if p == None or q == None:
                if p == q:
                    return True
                else:
                    return False
            if p.val != q.val:
                return False
            else:
                return dg(p.left, q.left) and dg(p.right, q.right)

        return dg(p, q)