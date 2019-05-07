#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 104_Maximum_Depth_of_Binary_Tree
# @Author  : TCY
# @Time    : 2019/5/6 14:47
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
    def maxDepth(self, root: TreeNode) -> int:
        """用递归实现
        1. 递归出口
        2. 递归主体。当点节点的高度 = max(左子树高度，右子树高度) + 1
        """
        if root == None:
            return 0
        elif root.right == None and root.left == None:
            return 1
        else:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        """采用广度优先遍历
        1. 特殊情况判断
        2. 初始化队列和其他数据
        3. 队列非空，弹出当前栈中节点的同时，将其非空子节点入队，完成时深度加1
        4. 深度减1(到叶子部分时候没有子节点，但是深度加了1),返回hight
        if not root:
            return 0
        q = queue.Queue()
        q.put(root)
        hight = 1
        while not q.empty():
            n = q.qsize()
            for i in range(n):
                tmp = q.get()
                if tmp.left:
                    q.put(tmp.left)
                if tmp.right:
                    q.put(tmp.right)
            hight += 1
        hight -= 1
        return hight
        """
