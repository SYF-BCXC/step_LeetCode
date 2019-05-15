#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 303_Range_Sum_Query-Immutable
# @Author  : TCY
# @Time    : 2019/5/15 15:40
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm


class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.r = [0 for _ in range(self.n + 1)]
        tmp = 0
        for i in range(1, self.n + 1):
            tmp += nums[i - 1]
            self.r[i] = tmp

    def sumRange(self, i: int, j: int) -> int:
        if i > j or i < 0 or j >= self.n:
            return 0
        return self.r[j + 1] - self.r[i]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)