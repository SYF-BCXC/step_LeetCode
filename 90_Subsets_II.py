#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 90_Subsets_II
# @Author  : TCY
# @Time    : 2019/5/23 11:04
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = [[]]

        def helper(i, item):
            if i >= n:
                return
            item.append(nums[i])
            if item not in ans:
                ans.append(item[:])
            helper(i + 1, item)
            item.pop()
            helper(i + 1, item)

        helper(0, [])
        return ans
