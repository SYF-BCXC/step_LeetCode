#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 013_ Roman_to_Integer
# @Author  : TCY
# @Time    : 2018/9/27 15:30
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm

"""
题目描述:
https://leetcode-cn.com/problems/roman-to-integer/description/
思路:
1、将字符串直接按照对应值进行处理，唯一需要注意的是是否出现那6种特殊情况
2、 反转字符串，并利用I 对应值小于 V这个信息，如果小于了直接减去 I 的值
"""


class Solution:
    def romanToInt(self, s):
        result, len_s, x = 0, len(s), 0
        while x < (len_s - 1):
            z = s[x]
            if z == 'M':
                result += 1000
                x += 1
            elif z == 'D':
                result += 500
                x += 1
            elif z == 'C':
                if s[x + 1] == 'D':
                    result += 400
                    x += 2
                elif s[x + 1] == 'M':
                    result += 900
                    x += 2
                else:
                    result += 100
                    x += 1
            elif z == 'L':
                result += 50
                x += 1
            elif z == 'X':
                if s[x + 1] == 'L':
                    result += 40
                    x += 2
                elif s[x + 1] == 'C':
                    result += 90
                    x += 2
                else:
                    result += 10
                    x += 1
            elif z == 'V':
                result += 5
                x += 1
            else:
                if s[x + 1] == 'V':
                    result += 4
                    x += 2
                elif s[x + 1] == 'X':
                    result += 9
                    x += 2
                else:
                    result += 1
                    x += 1
        if x == len_s:
            return result
        else:
            z = s[-1]
            if z == 'M':
                result += 1000
            elif z == 'D':
                result += 500
            elif z == 'C':
                result += 100
            elif z == 'L':
                result += 50
            elif z == 'X':
                result += 10
            elif z == 'V':
                result += 5
            else:
                result += 1
            return result

    # 方法二：代码更短，思路更清晰，不需要像方法一处理最后一个字符
    def romanToInt2(self, s):
        roman = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        carry = 0
        res = 0
        for letter in s[::-1]:
            cur = roman[letter]
            if cur >= carry:
                res += cur
            else:
                res -= cur
            carry = max(cur, carry)
        return res


if __name__ == '__main__':
    print(Solution().romanToInt("MCMXCIV"))
