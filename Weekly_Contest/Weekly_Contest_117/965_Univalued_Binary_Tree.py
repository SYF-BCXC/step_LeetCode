#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 965_Univalued_Binary_Tree
# @Author  : TCY
# @Time    : 2019/8/11 20:55
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root:
            return True
        self.flag = root.val
        self.ans = True

        def dfs(node):
            if node.val != self.flag:
                self.ans = False
                return
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)

        dfs(root)
        return self.ans