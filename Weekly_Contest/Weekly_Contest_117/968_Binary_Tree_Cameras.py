#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 968_Binary_Tree_Cameras
# @Author  : TCY
# @Time    : 2019/8/11 20:57
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


"""
思路：贪心。从叶节点往上找，如果存在父节点则尽量将相机放父节点上，然后依次往上递推。
一共存在三种情况：
0\ 节点未被监视，需要在其父节点放置相机
1\ 节点被监视，且相机就在本身
2\ 节点被监视，且相机在其子节点
"""


class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        self.ans = 0

        def dfs(node):
            if node.left == None and node.right == None:
                return 0
            covered = 0
            needCamera = 0
            if node.left:
                state = dfs(node.left)
                if state == 0:
                    needCamera += 1
                elif state == 1:
                    covered += 1
            if node.right:
                state = dfs(node.right)
                if state == 0:
                    needCamera += 1
                elif state == 1:
                    covered += 1
            if needCamera > 0:
                self.ans += 1
                return 1
            if covered > 0:
                return 2
            return 0

        state = dfs(root)
        if state == 0:
            self.ans += 1
        return self.ans

