#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 1052_Grumpy_Bookstore_Owner
# @Author  : TCY
# @Time    : 2019/5/27 16:42
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm

# 比赛时的写法还是太过于啰嗦了，完全不用gain数组，直接滑动就行，如果是生气变为不生气则为该滑动窗口的收益，最后保存最大收益，再加上base的收益就行了

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        """计算一个收益数组"""
        n = len(customers)
        gain = []
        for i in range(n):
            if grumpy[i] == 1:
                gain.append(customers[i])
            else:
                gain.append(0)
        mxi, mxj = 0, X - 1
        mx = 0
        i, j = 0, X - 1
        while j < n:
            tmp = sum(gain[i:j + 1])
            if tmp > mx:
                mxi, mxj = i, j
                mx = tmp
            i += 1
            j += 1
        """计算最后的满意顾客数量"""
        while mxi <= mxj:
            grumpy[mxi] = 0
            mxi += 1
        ans = 0
        for i in range(n):
            if grumpy[i] == 0:
                ans += customers[i]
        return ans
