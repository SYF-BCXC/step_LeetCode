#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 1026_Maximum_Difference_Between_Node_and_Ancestor
# @Author  : TCY
# @Time    : 2019/8/10 11:20
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        def dfs(node):
            res, high, low = 0, float('-inf'), float('inf')
            if node.left:
                r, h, l = dfs(node.left)
                high = max(h, high)
                low = min(l, low)
                res = max(res, r)
            if node.right:
                r, h, l = dfs(node.right)
                high = max(h, high)
                low = min(l, low)
                res = max(res, r)
            res = max(res, node.val - low, high - node.val)
            high = max(high, node.val)
            low = min(low, node.val)
            return res, high, low

        return dfs(root)[0]
