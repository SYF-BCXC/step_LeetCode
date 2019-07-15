#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 236_Lowest_Common_Ancestor_of_a_Binary_Tree
# @Author  : TCY
# @Time    : 2019/7/15 12:54
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm

"""最近公共祖先。左右各一个节点，本身是一个节点左右含另外一个"""


class Solution:
    def helper(self, root, p, q):
        if not root:
            return 0, 0, 0

        mm = 0
        if root == p:
            mm += 1
        if root == q:
            mm += 1

        ll, lm, lr, rl, rm, rr = 0, 0, 0, 0, 0, 0
        if root.left:
            ll, lm, lr = self.helper(root.left, p, q)
        if root.right:
            rl, rm, rr = self.helper(root.right, p, q)

        l = ll + lm + lr
        r = rl + rm + rr
        if (l + r + mm) == 2 and l != 2 and r != 2:
            self.ans = root

        return l, mm, r

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = None
        self.helper(root, p, q)
        return self.ans