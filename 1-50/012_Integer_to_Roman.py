#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 012_Integer_to_Roman
# @Author  : TCY
# @Time    : 2018/9/27 11:53
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm

"""
题目描述:
https://leetcode-cn.com/problems/integer-to-roman/description/
字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
输入确保在 1 到 3999 的范围内。
思路:
1、直接处理，依次拿到每一位的值，并转换

"""


class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # 先拿到每一位
        list_num, len_num, result = [], len(str(num)), ''
        for i in range(len_num - 1, -1, -1):
            temp = num // (10 ** i)
            list_num.append(temp)
            num -= temp * (10 ** i)

        # list_num [3, 2, 6, 4]
        # return str
        def q_trans(num):
            return 'M' * num

        def b_trans(num):
            if num == 4:
                return 'CD'
            if num == 9:
                return 'CM'
            if num >= 5:
                return 'D' + 'C' * (num - 5)
            else:
                return 'C' * num

        def s_trans(num):
            if num == 4:
                return 'XL'
            if num == 9:
                return 'XC'
            if num >= 5:
                return 'L' + 'X' * (num - 5)
            else:
                return 'X' * num

        def g_trans(num):
            if num == 4:
                return 'IV'
            if num == 9:
                return 'IX'
            if num >= 5:
                return 'V' + 'I' * (num - 5)
            else:
                return 'I' * num

        def control(num, l):
            if l == 0:
                return g_trans(num)
            elif l == 1:
                return s_trans(num)
            elif l == 2:
                return b_trans(num)
            else:
                return q_trans(num)

        for x, z in enumerate(list_num[::-1]):
            result = control(z, x) + result
        return result


if __name__ == '__main__':
    print(Solution().intToRoman(1994))
