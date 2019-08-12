#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 958_Check_Completeness_of_a_Binary_Tree
# @Author  : TCY
# @Time    : 2019/8/11 9:59
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import queue


class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        q = queue.Queue()
        cur = root
        while cur:
            q.put(cur.left)
            q.put(cur.right)
            cur = q.get()
        while not q.empty():
            if q.get() == None:
                continue
            else:
                return False
        return True
