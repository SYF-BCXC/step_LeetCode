#!/usr/bin/python3

# @Project = leetCode
# @File    : 3_Longest_Substring_Without_Repeating_Characters
# @Author  : TCY
# @Time    : 2018/9/15 19:02
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm
"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        if length == 0:
            return 0
        elif length == 1:
            return 1
        else:
            b = 0
            myList = [s[0]]
            temp = 1
            while b < (length-1):
                if s[b+1] not in myList:
                    # 如果不在里面，将该元素加入list，并重新计算最大temp
                    b += 1
                    myList.append(s[b])
                    if len(myList)>temp:
                        temp = len(myList)
                else:
                    # 如果在里面，将该元素在list中位置以前的(包括该位置)都删除，将该元素加入list
                    loc = myList.index(s[b+1])
                    myList = myList[loc+1:]+[s[b+1]]
                    b = b+1
            return temp


if __name__ == '__main__':
    inString = input("请输入字符串:")
    print(Solution().lengthOfLongestSubstring(inString))

""" 最快参考代码
class Solution:
    def lengthOfLongestSubstring(self, s):
        sub = ''
        sub_len = 0
        max_len = 0
        max_sub = ''
        for letter in s:
            if letter in sub:
                if sub_len > max_len:
                    max_len = sub_len
                    max_sub = sub
                index = sub.index(letter)
                sub = sub[index + 1:] + letter
                sub_len = sub_len - index
            else:
                sub = sub + letter
                sub_len += 1
        if sub_len > max_len:
            max_len = sub_len
        return max_len
"""
