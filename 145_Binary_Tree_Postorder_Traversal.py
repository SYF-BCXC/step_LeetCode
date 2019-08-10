#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 145_Binary_Tree_Postorder_Traversal
# @Author  : TCY
# @Time    : 2019/7/19 17:12
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

"""后序遍历
思路1：用两个栈，模仿前序遍历，把左右根的顺序改为根右左，因此先压左再压右，最后将结果逆序(其中一个栈的作用)
思路2：用一个栈，两个变量h和c,h代表最近一次打印的节点，c代表当栈顶节点。主要有三种情况：1，c的左孩子不为空，且h不为c的左孩子，将c.left压入栈中，c变为c.left。 2. C的右孩子不为空，且H不为C的有孩子，将c.right压入栈中，c变为c.right.
3. c的左孩子右孩子均为空或者h为c的孩子，则打印c，c=stack.pop()
注意事项：
"""


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        """非递归。一个栈"""
        if not root:
            return []
        stack = [root]
        h = root
        c = None
        ans = []
        while stack:
            c = stack[-1]
            if c.left and c.left != h and c.right != h:
                stack.append(c.left)
            elif c.right and c.right != h:
                stack.append(c.right)
            else:
                ans.append(c.val)
                h = c
                stack.pop()
        return ans


"""
非递归。两个栈
if not root:
            return []

        stack_1 = [root]
        stack_2 = []
        ans = []

        while stack_1:
            cur = stack_1.pop()
            stack_2.append(cur.val)
            if cur.left:
                stack_1.append(cur.left)
            if cur.right:
                stack_1.append(cur.right)
        ans = stack_2[::-1]
        return ans"""
