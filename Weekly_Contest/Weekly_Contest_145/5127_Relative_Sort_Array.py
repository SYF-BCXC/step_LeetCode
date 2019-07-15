#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 5127_Relative_Sort_Array
# @Author  : TCY
# @Time    : 2019/7/14 18:02
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm


from collections import Counter
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        c = Counter(arr1)
        ans = []
        for i in range(len(arr2)):
            for j in range(c[arr2[i]]):
                ans.append(arr2[i])
            c.pop(arr2[i])
        tmp = sorted(c.items(), key=lambda x:x[0])
        for a, b in tmp:
            for k in range(b):
                ans.append(a)
        return ans