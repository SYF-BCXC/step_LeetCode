#!/usr/bin/python3

# @Project = leetCode
# @File    : 6_ZigZag_Conversion
# @Author  : TCY
# @Time    : 2018/9/22 14:56
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm
"""
题目描述:
https://leetcode-cn.com/problems/zigzag-conversion/description/

思路:
法1、（最直接最暴力，毫无技巧，费时）首先转置操作，字符串分组处理。每组 (numRows-1)*2 个，返回 numRows-1 行，即list。最后处理一下边界即可。
法2、 类似于俄罗斯方块下降，第一次落在第一堆，第二次第二堆，第numRows+1 次，落在numRows-1 堆
"""


class Solution:
    def zigZag(self, s, numRows):
        """
        前[0,numRows-1]个放第一行，第二行的 -2 位置放第 [numRows] 个，第三行的 -3 位置放第 [numRows+1]...
        返回numRows-1行
        """
        temp = []
        for i in range(numRows - 1):
            if i == 0:
                l1 = list(s[0:numRows])
                temp.append(l1)
            else:
                temp.append(["#" for j in range(numRows)])
                temp[i][-i - 1] = s[numRows + i - 1]
        return temp

    def convert1(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if not s:
            return s
        if numRows==1:
            return s
        temp = []
        maxlen = len(s)
        groupLen = (numRows-1)*2
        group, left = divmod(maxlen, groupLen)
        for i in range(group):
            temp.extend(self.zigZag(s[i*groupLen:(i+1)*groupLen], numRows))
        if left > 0:
            if left <= numRows:
                temp.append(list(s[(group)*groupLen:]))
                temp[-1].extend(["#" for i in range(numRows-left)])
            else:
                temp.append(list(s[(group) * groupLen:(group) * groupLen+numRows]))
                left -= numRows
                for i in range(left):
                    temp.append(["#" for j in range(numRows)])
                    temp[-1][-i-2] = s[i-left]
        #开始读取字符串
        my_str = ""
        for i in range(numRows):
            for j in range(len(temp)):
                if temp[j][i]!="#":
                    my_str += temp[j][i]
        return my_str

    def convert2(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s

        index, step = 0, 1
        l = [""] * numRows

        for item in s:
            l[index] += item
            if index == 0:
                step = 1
            if index == numRows - 1:
                step = -1
            index += step

        return "".join(l)


if __name__ == '__main__':
    s = "AAAABB"
    print(Solution().convert2(s, 3))
