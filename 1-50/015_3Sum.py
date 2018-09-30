#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 015_3Sum
# @Author  : TCY
# @Time    : 2018/9/28 23:06
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm

"""
题目描述:
https://leetcode-cn.com/problems/3sum/description/
思路:
1、暴力法。O(n^3)，时间复杂度太高
（构思，暂未实现）2、排序后，用双指针法。指针分别指向a和b，设有abs(a)>abs(b)。
    若abs(a)>2*abs(b)，则a的指针+1
    若abs(a) == 2*abs(b)，则 若b的指针-1等于b，有一组返回值
    若abs(a) < 2*abs(b)，则b的指针靠内搜索
    直到两个指针重合，搜索完成
3、从左到右扫描，然后以这个数为根据，在后面的数据中用双指针找到另外两个
4、
"""

import collections

class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums, result, i = sorted(nums), [], 0
        while i < len(nums) - 2:
            if i == 0 or nums[i] != nums[i - 1]:
                j, k = i + 1, len(nums) - 1
                while j < k:
                    if nums[i] + nums[j] + nums[k] < 0:
                        j += 1
                    elif nums[i] + nums[j] + nums[k] > 0:
                        k -= 1
                    else:
                        result.append([nums[i], nums[j], nums[k]])
                        j, k = j + 1, k - 1
                        while j < k and nums[j] == nums[j - 1]:
                            j += 1
                        while j < k and nums[k] == nums[k + 1]:
                            k -= 1
            i += 1
        return result

    def threeSum2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        d = collections.Counter(nums)
        nums_2 = [x[0] for x in d.items() if x[1] > 1]
        nums_new = sorted([x[0] for x in d.items()])
        rtn = [[0, 0, 0]] if d[0] >= 3 else []
        for i, j in enumerate(nums_new):
            if j <= 0:
                numss2 = nums_new[i + 1:]
                for x, y in enumerate(numss2):
                    if 0 - j - y in [j, y] and 0 - j - y in nums_2:
                        if sorted([j, y, 0 - j - y]) not in rtn:
                            rtn.append(sorted([j, y, 0 - j - y]))
                    if 0 - j - y not in [j, y] and 0 - j - y in nums_new:
                        if sorted([j, y, 0 - j - y]) not in rtn:
                            rtn.append(sorted([j, y, 0 - j - y]))
        return rtn


if __name__ == '__main__':
    print(Solution().threeSum())