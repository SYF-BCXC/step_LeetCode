#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 94_Binary_Tree_Inorder_Traversal
# @Author  : TCY
# @Time    : 2019/7/15 12:53
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""递归写法
        self.ans = []
        def inorder(r):
            if not r:
                return
            if r.left:
                inorder(r.left)

            self.ans.append(r.val)

            if r.right:
                inorder(r.right)

        inorder(root)
        return self.ans"""


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """非递归写法。关键：两个while，
        第一个while，当前节点不为空  或者  栈不为空，执行整个过程
        第二个while，让当前节点到最左下角
        主逻辑： 每个节点走到左下角，且其路径压入栈。栈pop，访问，压入其右节点，继续主逻辑
        """
        ans = []
        if not root:
            return ans
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            ans.append(cur.val)
            cur = cur.right
        return ans
