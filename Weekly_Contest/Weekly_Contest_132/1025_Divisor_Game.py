#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 1025_Divisor_Game
# @Author  : TCY
# @Time    : 2019/8/10 11:19
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm

class Solution:
    def divisorGame(self, N: int) -> bool:
        if N == 1:
            return False
        if N == 2:
            return True
        if N == 3:
            return False
        if N == 4:
            return True
        return N % 2 == 0
