#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 139_Word_Break_1
# @Author  : TCY
# @Time    : 2019/5/5 9:51
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """动态规划法.dp[i]表示[0,i)的部分是否可以分割"""
        dp = [True]
        for i in range(1, len(s) + 1):
            tmp = s[0:i] in wordDict
            for j in range(1, len(dp)):
                tmp = tmp or (dp[j] and s[j:i] in wordDict)
            dp.append(tmp)
        return dp[len(s)]


"""小Trick,如果长度小于wordList里的最小值或者大于wordList里的最大值，则判断inDict"""




