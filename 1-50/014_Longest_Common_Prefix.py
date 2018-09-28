#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 014_Longest_Common_Prefix
# @Author  : TCY
# @Time    : 2018/9/27 16:04
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm

"""
题目描述:
https://leetcode-cn.com/problems/longest-common-prefix/description/
思路:
1、直接扫描匹配即可，此题较为简单
"""


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        temp = 0
        for i in range(len(strs[0])):
            for j in range(len(strs)):
                if i >= len(strs[j]):
                    return strs[0][:temp]
                if strs[0][i] == strs[j][i]:
                    continue
                else:
                    return strs[0][:temp]
            temp += 1
        return strs[0][:temp]

    # 最快解答
    def longestCommonPrefix2(self, strs):
        if not strs:
            return ""
        shortest = min(strs, key=len)
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
        return shortest


if __name__ == '__main__':
    print(Solution().longestCommonPrefix2(["aa", "a", "a"]))
