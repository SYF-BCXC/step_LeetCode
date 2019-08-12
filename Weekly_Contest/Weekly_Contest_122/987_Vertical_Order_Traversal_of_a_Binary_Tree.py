#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 987_Vertical_Order_Traversal_of_a_Binary_Tree
# @Author  : TCY
# @Time    : 2019/8/13 0:17
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections
class Solution:

    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        self.h = collections.defaultdict(list)

        def dfs(node, m, h):
            self.h[m].append((h, node.val))
            if node.left:
                dfs(node.left, m - 1, h + 1)
            if node.right:
                dfs(node.right, m + 1, h + 1)

        dfs(root, 0, 0)

        keys = list(self.h.keys())
        keys.sort()
        ans = []
        for i in keys:
            self.h[i].sort()
            tmp = []
            for j in self.h[i]:
                tmp.append(j[1])
            ans.append(tmp)
        return ans

