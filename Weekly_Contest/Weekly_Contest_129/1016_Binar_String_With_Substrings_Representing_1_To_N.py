#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 1016_Binar_String_With_Substrings_Representing_1_To_N
# @Author  : TCY
# @Time    : 2019/4/27 15:16
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm

""" 最快解答
1. N到N~2的部分能表示，肯定能表示1~N//2，因为只多了一位1
2. bin(2) => '0b10'

class Solution:
    def queryString(self, S: str, N: int) -> bool:
        for i in range(N, N // 2, -1):
            if not bin(i)[2:] in S:
                return False
        return True
"""


class Solution:
    def queryString(self, S: str, N: int) -> bool:
        """N <= 10^9，因此最长30位(1024=2^10)
        S串长度位1000，每个位置往后算他30位，因此最多可以表示30*1000个数字，也就是3e4个，而总共要求能表示1~N个数字，所以当N大于3e4时，必然是不可能的
        """
        if N > 30000:
            return False
        vis = [False for _ in range(30050)]

        """遍历获取子串，并再vis中打上标记"""
        for i in range(len(S)):
            for j in range(30):
                tmp = int(S[i:i + j + 1], 2)
                if tmp > N:
                    pass
                else:
                    vis[tmp] = True
        for i in range(1, N + 1):
            if vis[i] == False:
                return False
        return True


