#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 971_Flip_Binary_Tree_To_Match_Preorde_Traversal
# @Author  : TCY
# @Time    : 2019/8/12 15:03
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        self.ans = []
        self.i = 0

        def dfs(node, v):
            if not node:
                return True
            if node.val != v[self.i]:
                return False
            self.i += 1
            if node.left and node.left.val == v[self.i]:
                return dfs(node.left, v) and dfs(node.right, v)
            elif node.right and node.right.val == v[self.i]:
                if node.left:
                    self.ans.append(node.val)
                return dfs(node.right, v) and dfs(node.left, v)
            return node.left == None and node.right == None

        if dfs(root, voyage):
            return self.ans
        else:
            return [-1]


"""            if not voyage:
                return False
            if node.val != voyage[0]:
                return False
            if node.left and not node.right:
                node.left, node.right = node.right, node.left

            l_val, l_loc = -1,0
            r_val, r_loc = -1,0
            if node.left:
                l_val = node.left.val
            if node.right:
                r_val = node.right.val
            for loc,val in enumerate(voyage):
                if val == r_val:
                    r_loc = loc
                if val == l_val:
                    l_loc = loc
            if l_loc > r_loc:
                self.ans.append(node.val)
                node.left, node.right = node.right, node.left

            r_ans, l_ans = True, True
            if node.right:
                r_ans = dfs(node.right, voyage[max(l_loc,r_loc):])
            if node.left:
                l_ans = dfs(node.left, voyage[1:max(l_loc,r_loc)])
            #print(l_ans, r_ans)
            if r_ans and l_ans:
                return True
            else:
                return False
        if dfs(root, voyage):
            return self.ans
        else:
            return [-1]"""

