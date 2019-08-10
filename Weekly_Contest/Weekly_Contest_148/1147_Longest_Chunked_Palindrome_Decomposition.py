#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 1147_Longest_Chunked_Palindrome_Decomposition
# @Author  : TCY
# @Time    : 2019/8/10 0:06
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm


"""
输入：text = "ghiabcdefhelloadamhelloabcdefghi"
输出：7
解释：我们可以把字符串拆分成 "(ghi)(abcdef)(hello)(adam)(hello)(abcdef)(ghi)"。最大段数为7

思路：
1、贪心.
2、动态规划.
"""


# solution 1
def longestDecomposition(S):
    res, l, r = 0, "", ""
    for i, j in zip(S, S[::-1]):
        l, r = l + i, j + r
        if l == r:
            res, l, r = res + 1, "", ""
    return res


# solution 2
import collections


def longestDecomposition2(S: str) -> int:
    n = len(S)
    c1, c2 = collections.Counter(), collections.Counter()
    dp = {0: 0}
    for j in range(n // 2):
        c1[S[j]] += 1
        c2[S[n - 1 - j]] += 1
        if c1 != c2:
            continue
        dp[j + 1] = 0
        for i in dp:
            if i == j + 1:
                continue
            if S[i:j + 1] == S[n - j - 1:n - i]:
                dp[j + 1] = max(dp[j + 1], dp[i] + 2)
    mid = (n + 1) // 2
    return dp.get(mid, max(dp.values()) + 1)
