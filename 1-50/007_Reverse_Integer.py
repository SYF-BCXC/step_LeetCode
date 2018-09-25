#!/usr/bin/python3

# @Project = leetCode
# @File    : 7_Reverse_Integer
# @Author  : TCY
# @Time    : 2018/9/22 21:18
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm

"""
题目描述:
https://leetcode-cn.com/problems/reverse-integer/description/
思路:
1、转换成string，然后[::-1]
2、利用除法，获取不同位上的值
"""


class Solution:
    def reverse1(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = 0
        if x < 0:
            x = -x
            flag = 1
        x_str = str(x)
        x_str = x_str[::-1]
        x = int(x_str)
        if flag:
            x = -x
        if abs(x) > 0x7FFFFFFF:
            return 0
        return x

    def reverse2(self, x):
        a = abs(x)
        r = 0
        while a:
            r = r * 10 + a % 10
            a = a // 10
        if x < 0:
            r = -r
        if abs(r) > 0x7FFFFFFF:
            return 0
        return r


if __name__ == '__main__':
    print(Solution().reverse1(39979))
