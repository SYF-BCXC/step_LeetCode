#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 1015_Smallest_Integer_Divisible_by_K
# @Author  : TCY
# @Time    : 2019/4/27 14:08
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm

class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        """增加1的过程是固定的，其余数跟着变就行了.
        例如:11 = 3*3 + 2
        111 = (3*3+2)*10 + 1 = 3*_ + 20+1 ，然后只考虑21能否被3整除
        """
        if K % 2 == 0:
            return -1
        yu = 1 % K
        L = 1
        xunhuan = [False for _ in range(K + 5)]
        xunhuan[1] = True
        while yu != 0:
            L += 1
            yu = (yu * 10 + 1) % K
            if yu == 0:
                return L
            else:
                if xunhuan[yu]:
                    return -1
                else:
                    xunhuan[yu] = True
        return L
