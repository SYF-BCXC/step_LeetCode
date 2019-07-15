#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 5128_Lowest_Common_Ancestor_of_Deepest_Leaves
# @Author  : TCY
# @Time    : 2019/7/14 22:31
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


"""
树-》递归-》减少问题规模
"""


class Solution:
    def helper(self, root, d):
        """左节点的深度等于右节点深度等于最深深度则为ans"""
        if d > self.mx:
            self.mx = d
        l = d
        r = d

        # 求左右节点最深深度
        if root.left:
            l = self.helper(root.left, d + 1)
        if root.right:
            r = self.helper(root.right, d + 1)

        # 左右深度都是最大则为ans
        if l == self.mx and r == self.mx:
            self.res = root

        # 返回当前节点子孙节点的最深深度
        return max(l, r)

    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        self.mx = 0
        self.res = None
        self.helper(root, 1)
        return self.res