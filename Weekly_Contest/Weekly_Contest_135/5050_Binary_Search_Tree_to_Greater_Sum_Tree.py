#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 5050_Binary_Search_Tree_to_Greater_Sum_Tree
# @Author  : TCY
# @Time    : 2019/5/6 10:37
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        """更大和树的中序遍历为递减"""
        zhongTree = []  # 记录中序遍历的树的节点

        def midTra(now):
            if now.left:
                midTra(now.left)
            zhongTree.append(now)
            if now.right:
                midTra(now.right)

        midTra(root)
        for i in range(len(zhongTree) - 1, -1, -1):
            if i != len(zhongTree) - 1:
                zhongTree[i].val += zhongTree[i + 1].val
        return root
