#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 1144_Decrease_Elements_To_Make_Array_Zigzag
# @Author  : TCY
# @Time    : 2019/8/9 20:35
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm

"""
精简答案：
def movesToMakeZigzag(self, A):
    A = [float('inf')] + A + [float('inf')]
    res = [0, 0]
    for i in xrange(1, len(A) - 1):
        res[i % 2] += max(0, A[i] - min(A[i - 1], A[i + 1]) + 1)
    return min(res)

所学招式：
1、 float('inf') -> 正无穷; float('-inf') -> 负无穷
2、 灵活运用i%2获得奇偶位置。
"""

class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        """只有两种可能，遍历即可"""
        """偶数位置大,让奇数位置减少"""
        n = len(nums)
        ans1 = 0
        ans2 = 0
        for i in range(n):
            if i % 2 == 1:
                tmp = 0
                if i == n - 1:
                    tmp = nums[i - 1]
                else:
                    tmp = min(nums[i - 1], nums[i + 1])
                if nums[i] >= tmp:
                    ans1 += nums[i] - tmp + 1
            else:
                tmp = 0
                if i == 0:
                    tmp = nums[i + 1]
                elif i == n - 1:
                    tmp = nums[i - 1]
                else:
                    tmp = min(nums[i - 1], nums[i + 1])
                if nums[i] >= tmp:
                    ans2 += nums[i] - tmp + 1
        return min(ans1, ans2)


