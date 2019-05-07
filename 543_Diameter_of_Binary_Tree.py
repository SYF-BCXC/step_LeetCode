#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 543_Diameter_of_Binary_Tree
# @Author  : TCY
# @Time    : 2019/5/6 15:39
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def __init__(self):
        self.d = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        """递归。
        1. 同130题类似。成员属性记录结果，一个递归函数递归深度。
        """
        self.maxHight(root)
        return self.d

    def maxHight(self, root):
        if root == None:
            return 0
        l = self.maxHight(root.left)
        r = self.maxHight(root.right)
        if l + r > self.d:
            self.d = l + r
        return max(l, r) + 1

