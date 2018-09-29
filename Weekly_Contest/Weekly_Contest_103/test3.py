#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : test3
# @Author  : TCY
# @Time    : 2018/9/29 15:37
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm

"""
题目描述:
https://leetcode-cn.com/contest/weekly-contest-103/problems/smallest-range-ii/
思路:
1、直接以贪心策略 -K 和 +K 行不通。
2、非常精彩！先假设所有数据都已经-K，只需要选择一些数据去+2K (并且所有的数据都没有必要实际上去-K，因为需要的仅仅是差值)
"""


class Solution:
    def smallestRangeII(self, A, K):
        A.sort()
        org = A[-1] - A[0]
        if org <= K:
            return org
        top = A[-1] - K
        bot = A[0] + K
        if top < bot:
            top, bot = bot, top
        for i in range(len(A)):
            temp1 = A[i] + K
            temp2 = A[i] - K
            if bot <= temp1 <= top:
                A[i] = A[i] + K
            elif bot <= temp2 <= top:
                A[i] = A[i] - K
            else:
                if temp1 - top <= bot - temp2:
                    A[i] = A[i] + K
                    top = temp1
                else:
                    A[i] = A[i] - K
                    bot = temp2
        if org < top - bot:
            return org
        else:
            return top - bot

    def smallestRangeII2(self, A, K):
        # assume everything already -K so we pick some to +2K
        if not A:
            return 0
        A = sorted(set(A))
        K *= 2
        m = A[-1]
        r = A[-1] - A[0]
        for i in range(len(A) - 1):
            # 意思就是 A[i]-K > A[0]+K，则该数及其以后的数必定是需要-K的，而-K操作已经完成，因此直接break
            if A[i] >= A[0] + K:
                break
            m = max(m, A[i] + K)
            r = min(r, m - min(A[i + 1], A[0] + K))
        return r


if __name__ == '__main__':
    print(Solution().smallestRangeII(
        [8038, 9111, 5458, 8483, 5052, 9161, 8368, 2094, 8366, 9164, 53, 7222, 9284, 5059, 4375, 2667, 2243, 5329, 3111,
         5678, 5958, 815, 6841, 1377, 2752, 8569, 1483, 9191, 4675, 6230, 1169, 9833, 5366, 502, 1591, 5113, 2706, 8515,
         3710, 7272, 1596, 5114, 3620, 2911, 8378, 8012, 4586, 9610, 8361, 1646, 2025, 1323, 5176, 1832, 7321, 1900,
         1926, 5518, 8801, 679, 3368, 2086, 7486, 575, 9221, 2993, 421, 1202, 1845, 9767, 4533, 1505, 820, 967, 2811,
         5603, 574, 6920, 5493, 9490, 9303, 4648, 281, 2947, 4117, 2848, 7395, 930, 1023, 1439, 8045, 5161, 2315, 5705,
         7596, 5854, 1835, 6591, 2553, 8628], 4643))
