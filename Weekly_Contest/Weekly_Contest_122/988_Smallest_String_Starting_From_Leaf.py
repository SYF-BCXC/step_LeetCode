#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 988_Smallest_String_Starting_From_Leaf
# @Author  : TCY
# @Time    : 2019/8/13 0:16
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']

        def dfs(node, item):
            if node.left == None and node.right == None:
                return alpha[node.val] + item
            item = alpha[node.val] + item
            left, right = item, item
            if node.left:
                left = dfs(node.left, item)
            if node.right:
                right = dfs(node.right, item)
            if left == item:
                return right
            if right == item:
                return left
            return min(left, right)

        return dfs(root, '')