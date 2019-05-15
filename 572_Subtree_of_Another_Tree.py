#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 572_Subtree_of_Another_Tree
# @Author  : TCY
# @Time    : 2019/5/10 10:37
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        """双层递归"""
        # Edge case
        if not s or not t:
            return False

        # process
        def helper(a, b):
            if not a or not b:
                return not a and not b

            if a.val != b.val:
                return False

            return helper(a.left, b.left) and helper(a.right, b.right)

        # recursion
        return helper(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)


""" 最快解答
class Solution:
    def isSubtree(self, s: 'TreeNode', t: 'TreeNode') -> 'bool':
        def dfs(a, b):
            if not a or not b:
                return not a and not b

            if a.val == b.val and dfs(a.left, b.left) and dfs(a.right, b.right):
                return True

            if b is t:
                return dfs(a.left, t) or dfs(a.right, t)

            return dfs(a, t)

        return dfs(s, t)
"""

""" 树转字符串 (根)(左)(右)
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        s_tree = self.tree2str(s)
        t_tree = self.tree2str(t)
        #print(s_tree)
        #print(t_tree)
        # 如果是子串，则返回index，如果不是子串，则返回-1
        index = s_tree.find(t_tree)
        if index == -1:
            return False
        else:
            return True

    def tree2str(self, t: TreeNode) -> str:
        if not t:
            return ''
        res = '(' + str(t.val) + ')'
        left = self.tree2str(t.left)
        right = self.tree2str(t.right)

        if left == '' and right == '':  # 如果左右字节点为空，两个空括号
            res += '()()'
            return res
        elif left == '':  # 如果左节点为空，则需要为左节点添加空括号，然后括号+右子树
            res += '()' + '(' + right + ')'
        elif right == '':  # 如果右结点为空，则只需括号+左子树
            res += '(' + left + ')' +'()'
        else:  # 如果左右子树都不为空，则添加左右子树
            res += '(' + left + ')' + '(' + right + ')'
        return res

"""