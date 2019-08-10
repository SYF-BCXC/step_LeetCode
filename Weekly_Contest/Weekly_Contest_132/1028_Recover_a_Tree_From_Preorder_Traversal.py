#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 1028_Recover_a_Tree_From_Preorder_Traversal
# @Author  : TCY
# @Time    : 2019/8/10 11:21
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        stack = []
        i = 0
        while i < len(S):
            level = 0
            while S[i] == '-':
                level += 1
                i += 1
            strx = ''
            while i < len(S) and S[i] != '-':
                strx += S[i]
                i += 1
            x = int(strx)

            while len(stack) > level:
                stack.pop()
            node = TreeNode(x)
            if stack:
                if stack[-1].left == None:
                    stack[-1].left = node
                else:
                    stack[-1].right = node
            stack.append(node)
        return stack[0]
