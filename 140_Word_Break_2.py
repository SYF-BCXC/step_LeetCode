#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 140_Word_Break_2
# @Author  : TCY
# @Time    : 2019/5/5 9:51
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm


"""动态规划还超时了，超时用例：
"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
题目大致思路同139，讨论区说先用139的代码判断，可以再执行就能通过，但是觉得没意思就先留着吧
"""
class Solution:
    def wordBreak(self, s: str, wordDict):
        """结合139题，同样用递归或者动态规划
        combine('leetcode') = inDict('leetcode')
                            U combine('l') && inDict('eetcode')
                            U combine('le') && inDict('etcode')
                            ...
                            U combine('leetcod') && inDict('e')
        dp[i] = combine(s[:i])，即['cats and','cat sand'] if can be break else []
        """
        dp = [[]]
        n = len(s)
        for i in range(1, n + 1):
            """先看是否本身就在里面s[:i]"""
            tmp_res = []
            if s[:i] in wordDict:
                tmp_res.append(s[:i])
            for j in range(1, i):
                """combine(dp[j],'s[j:i]')"""
                if s[j:i] not in wordDict:
                    continue
                if dp[j]:
                    """如果dp[j]有内容，则直接combine"""
                    for k in dp[j]:
                        tmp_res.append(k + ' ' + s[j:i])
            dp.append(tmp_res)
        return dp[-1]



