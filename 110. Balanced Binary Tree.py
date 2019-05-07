#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 110. Balanced Binary Tree
# @Author  : TCY
# @Time    : 2019/5/6 15:21
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
        self.result = True

    def maxHight(self, root):
        if root == None:
            return 0
        else:
            l = self.maxHight(root.left)
            r = self.maxHight(root.right)
            if abs(l - r) > 1:
                self.result = False
            return max(l, r) + 1

    def isBalanced(self, root: TreeNode) -> bool:
        """递归。所有节点的左右子树高度相差不大于1。还是需要计算高度的。
        """
        self.maxHight(root)
        return self.result
