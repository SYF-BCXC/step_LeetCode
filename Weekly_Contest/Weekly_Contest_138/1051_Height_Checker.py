#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 1051_Height_Checker
# @Author  : TCY
# @Time    : 2019/5/27 16:44
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        aft = sorted(heights)
        ans = 0
        for i in range(len(aft)):
            if aft[i] != heights[i]:
                ans += 1
        return ans
