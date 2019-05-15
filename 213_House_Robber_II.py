#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 213_House_Robber_II
# @Author  : TCY
# @Time    : 2019/5/15 15:25
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm

class Solution:
    def rob(self, nums: List[int]) -> int:
        """同打家劫舍1，递推公式不变dp[i] = max(dp[i-2]+nums[i],dp[i-1]),一个从0到n-1，一个从1到n，然后取最大值"""
        if len(nums) == 0:
            return 0
        if 1 <= len(nums) <= 3:
            return max(nums)
        dp0 = [0 for _ in range(len(nums))]  # 从0开始到第i个房间
        dp1 = [0 for _ in range(len(nums))]  # 从1开始到第i个房间
        dp0[0] = nums[0]
        dp0[1] = max(nums[0], nums[1])
        dp1[1] = nums[1]
        dp1[2] = max(nums[1], nums[2])
        n = len(nums)
        for i in range(len(nums)):
            if 2 <= i < n - 1:
                dp0[i] = max(dp0[i - 2] + nums[i], dp0[i - 1])
            if 3 <= i < n:
                dp1[i] = max(dp1[i - 2] + nums[i], dp1[i - 1])
        return max(dp0[n - 2], dp1[n - 1])
