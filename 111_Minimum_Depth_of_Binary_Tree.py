#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 111_Minimum_Depth_of_Binary_Tree
# @Author  : TCY
# @Time    : 2019/5/10 11:07
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm


# Definition for a binary tree node.
# class TreeNode:
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
import queue


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        """层序遍历 或者 递归"""
        if root == None:
            return 0
        q = queue.Queue()
        # 1.初始化
        q.put(root)
        l = 0

        # 2. while not q.empty()
        while not q.empty():
            l += 1
            for i in range(q.qsize()):
                tmp = q.get()
                if not tmp.left and not tmp.right:
                    return l
                if tmp.left:
                    q.put(tmp.left)
                if tmp.right:
                    q.put(tmp.right)
        # except
        return 0xfffffff

        """
        def helper(r,l):
            if r == None:
                return 0xfffffff
            if not r.left and not r.right:
                return l
            return min(helper(r.left,l+1),helper(r.right,l+1))
        if root == None:
            return 0
        return helper(root,1)
        """
