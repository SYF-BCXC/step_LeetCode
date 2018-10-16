#!/usr/bin/python3

# @Project = LeetCode
# @File    : 020_Valid_Parentheses
# @Author  : TCY
# @Time    : 2018/10/16 21:02
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm

"""
题目描述:
https://leetcode-cn.com/problems/valid-parentheses/description/
思路:
1、 用栈存储匹配。扫描是左括号，则进栈。右括号，则与栈顶元素进行匹配，如果是同一类型，出栈，否则return false。扫描完成后，栈为空则return True。
"""
"""
关于python中栈的补充：
stack = []
stack.append()
stack.pop()
stack[-1]
"""


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        left = ['(', '{', '[']
        pair = {'(': ')', '{': '}', '[': ']'}
        for i in s:
            if i in left:
                stack.append(i)
            else:
                if not stack:
                    return False
                if i == pair[stack[-1]]:
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        else:
            return False

        # 最快写法，思路一样，但是更加精简老练
        def isValid2(self, s):
            if (s is None or len(s) == 0):
                return True
            if len(s) % 2 == 1:
                return False
            stack = []
            dictionary = {'(': ')', '[': ']', '{': '}'}
            for each in s:
                if each in dictionary:
                    stack.append(each)
                else:
                    if not stack or dictionary[stack.pop()] != each:
                        return False

            return stack == []


if __name__ == '__main__':
    print(Solution().isValid())
