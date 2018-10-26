#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 022_Generate_Parentheses
# @Author  : TCY
# @Time    : 2018/10/24 23:26
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm

"""
题目描述:
https://leetcode-cn.com/problems/generate-parentheses/description/
思路:
第一印象：组合数量应该是全排列，因此和 123 的全排列可能会有共同点，但是一直找不到合适的点。(可以继续思考)
后续想法：递归。
后续想法：同样类比出栈入栈的过程，左括号代表入栈，右括号代表出栈。问一共有多少种入栈出栈的方法。

思路1：DFS。还有左括号则+"("，当右括号剩余个数大于左括号则+")"，当括号都不剩余时，则生成了一组结果。(其中只要满足加括号的条件，两个都需要进行，以免漏掉一些解答)
"""


class Solution:
    def __init__(self):
        self.res = []

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.generateParenthesisIter('', n, n)
        return self.res

    def generateParenthesisIter(self, mtr, l, r):
        if l == 0 and r == 0:
            self.res.append(mtr)
        if l > 0:
            self.generateParenthesisIter(mtr + '(', l - 1, r)
        if r > 0 and r > l:
            self.generateParenthesisIter(mtr + ')', l, r - 1)


if __name__ == '__main__':
    print(Solution().generateParenthesis(3))
