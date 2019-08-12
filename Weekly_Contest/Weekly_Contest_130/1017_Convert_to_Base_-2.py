#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 1017_Convert_to_Base_-2
# @Author  : TCY
# @Time    : 2019/4/24 16:28
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm

"""
其实更重要是让余数为正即可(手算两个数即可)。
class Solution:
    def baseNeg2(self, N: int) -> str:
        if N == 0:
            return '0'
        ans = ''
        while N != 0:
            d = N % (-2)
            N = N // -2
            if d < 0:
                d += 2
                N += 1
            ans = str(d) + ans
        return ans
"""



import math

def baseNeg2(N):
    """
    :type N: int
    :rtype: str
    """
    if N == 0:
        return '0'
    result = ''
    while N != 1:
        tmp = N / (-2)  # 随后将tmp取上整
        tmp = int(math.ceil(tmp))
        b = N - tmp * (-2)
        N = tmp
        if N == 1:
            result = '1' + str(b) + result
            return result
        else:
            result = str(b) + result
    return result

print(baseNeg2(4))