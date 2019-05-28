#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 1047_Remove_All_Adjacent_Duplicates_In_String
# @Author  : TCY
# @Time    : 2019/5/27 16:46
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm


class Solution:
    def removeDuplicates(self, S: str) -> str:
        n = len(S)
        target = list(S)
        flag = False
        loc = 0
        while not flag:
            while loc < n - 1:
                if target[loc] == target[loc + 1]:
                    # 删除loc和loc+1
                    target.pop(loc)
                    target.pop(loc)
                    loc -= 1
                    n = len(target)
                    flag = True
                loc += 1
            flag = not flag
            loc = 0
        return ''.join(target)
