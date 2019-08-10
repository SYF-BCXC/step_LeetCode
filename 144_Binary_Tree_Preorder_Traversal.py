#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 144_Binary_Tree_Preorder_Traversal
# @Author  : TCY
# @Time    : 2019/7/19 17:02
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""非递归方法主要思路在于遵循了根左右的规律，先访问根，然后依次将右节点和左节点压入栈中，这样弹出来时保证了左右的规律，即根左右。"""

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        """非递归方法"""
        if not root:
            return []
        stack = [root]
        ans = []
        while stack:
            cur = stack.pop()
            ans.append(cur.val)
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
        return ans




        """递归方法"""
"""        ans = []
        def recursion(node):
            if not node:
                return
            ans.append(node.val)
            if node.left: 
                recursion(node.left)
            if node.right: 
                recursion(node.right)
        recursion(root)
        return ans"""