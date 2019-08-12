#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 1156_Swap_For_Longest_Repeated_Character_Substring
# @Author  : TCY
# @Time    : 2019/8/11 22:09
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm

"""
统计每个连续区间，最长串: 1、本身就是最长 2、中间夹了一个其他字符；
此外，注意 aabaa 和 ababa 的区别，aabaa不能加1，ababa能加1，所以要统计a的总共的数量是否超过两个较长的小段，即是否还有多余能调过来的a
"""

import collections
class Solution:
    def maxRepOpt1(self, text: str) -> int:
        count = []     # 或者一行代码. count = [[c,len(list(g))] for c,g in itertools.groupby(text)]
        k = [text[0], 0]
        for i in range(len(text)):
            if text[i] == k[0]:
                k[1] += 1
            else:
                count.append(k.copy())
                k[0] = text[i]
                k[1] = 1
        count.append(k.copy())

        c = collections.Counter(text)
        ans = 1
        for i in range(len(count)):
            if count[i][1] == 1:
                if 0 < i < len(count) - 1 and count[i - 1][0] == count[i + 1][0]:
                    tmp = count[i - 1][1] + count[i + 1][1]
                    if c[count[i - 1][0]] > tmp:
                        ans = max(tmp + 1, ans)
                    else:
                        ans = max(tmp, ans)
            else:
                if c[count[i][0]] > count[i][1]:
                    ans = max(count[i][1] + 1, ans)
                else:
                    ans = max(count[i][1], ans)

        return ans
