#!/usr/bin/python3

# @Project = leetCode
# @File    : 9_Palindrome_Number
# @Author  : TCY
# @Time    : 2018/9/24 15:19
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm

"""
题目描述:
https://leetcode-cn.com/problems/palindrome-number/description/
思路:
此题类似于第七题Reverse_Integer，思路同样可以参考
1、转换成string，然后[::-1]，这里多一个符号的处理
2、利用除法，获取不同位上的值
"""


class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        s = str(x)
        s_r = s[::-1]
        if s_r == s:
            return True
        else:
            return False


if __name__ == '__main__':
    print(Solution().isPalindrome(101))
