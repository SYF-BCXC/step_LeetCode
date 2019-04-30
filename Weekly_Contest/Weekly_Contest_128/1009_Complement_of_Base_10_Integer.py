#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 1009_Complement_of_Base_10_Integer
# @Author  : TCY
# @Time    : 2019/4/30 13:50
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm


class Solution:
    def bitwiseComplement(self, N: int) -> int:
        if N == 0:
            return 1
        s = bin(N)[2:]
        ans = ''
        for i in s:
            if i == '1':
                ans += '0'
            elif i == '0':
                ans += '1'
        return int(ans,2)