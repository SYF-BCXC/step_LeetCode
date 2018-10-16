#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 017_Letter_Combinations_of_a_Phone_Number
# @Author  : TCY
# @Time    : 2018/10/12 12:17
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm

"""
题目描述:
https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/description/
思路:
1、数字依次解析，每进来一个数字，将其对应的字母与已有的所有字符串想拼接即可
"""


class Solution:
    # 思路1，最快的也是这个思路，只不过把合并写成了函数
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        d_map, rst = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs',
                      '8': 'tuv', '9': 'wxyz'}, ['']
        for i in digits:
            tmp = []  # 每次进来都得清零
            for j in range(len(rst)):
                for m in d_map[i]:
                    tmp.append(rst[j] + m)
            rst = tmp
        return rst


if __name__ == '__main__':
    print(Solution().letterCombinations("23"))
