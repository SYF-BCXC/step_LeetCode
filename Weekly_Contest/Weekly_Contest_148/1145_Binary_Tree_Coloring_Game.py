# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        lr = [0, 0]
        def f(node):
            if not node:
                return 0
            left, right = f(node.left), f(node.right)
            if node.val == x:
                lr[0], lr[1] = left, right
            return left+right+1
        f(root)
        return max(max(lr), n-sum(lr)-1) > n/2