#!/usr/bin/python3

# @Project = leetCode
# @File    : 5_Longest_Palindromic_Substring
# @Author  : TCY
# @Time    : 2018/9/17 23:04
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm

"""
题目描述:
https://leetcode-cn.com/problems/longest-palindromic-substring/description/
思路:
# 思路1：暴力。找所有字串，每个字串reverse看是否相等
# 思路2：动态规划。找所有长度为1和2的回文串。然后扩展。(暂时未看懂，网上找的代码，如果有看懂的，还请不吝赐教)
# 思路3：中间扩展法。找中心位置向两边扩展，中间位置一共 2n-1 个
# 思路4：Manacher算法。(最快，时间复杂度 o(n))

关于Manacher算法的补充：
    Manacher算法的思路其实和KMP算法的思路类似，都是利用已经扫描过的对等的字符串的信息，减少匹配次数。其中最精彩的地方在于将任意长度的字符串变成奇数长度(2*N+1一定为奇数)
    参考文献：https://www.cnblogs.com/love-yh/p/7072161.html
    http://phoenixgs.cn/2017/06/22/manacher-%E7%AE%97%E6%B3%95/
"""


class Solution:
    # 动态规划法
    def longestPalindrome1(self, s):
        # 暴力法
        m = len(s) + 1
        str = ""
        str_len = 0
        for i in range(m):
            # i表示当前字串长度
            for j in range(m - i):
                # j表示当前字串起始位置
                temp = s[j:j + i]
                if temp == temp[::-1]:
                    if len(temp) > str_len:
                        str = temp
                        str_len = len(temp)
        return str

    def dynamic_programming(self, s, i, j):
        if j == i:
            self.p[i, j] = True
            return True
        elif j == (i + 1):
            if s[i] == s[j]:
                self.p[i, j] = True
                return True
            else:
                self.p[i, j] = False
                return False
        else:
            self.p[i, j] = self.dynamic_programming(s, i + 1, j - 1) and (s[i] == s[j])

    # 动态规划法
    def longestPalindrome2(self, s):
        str_length = len(s)
        max_length = 0
        start = 0
        for i in range(str_length):
            if i - max_length >= 1 and s[i - max_length - 1: i + 1] == s[i - max_length - 1: i + 1][::-1]:
                start = i - max_length - 1
                max_length += 2
                continue
            if i - max_length >= 0 and s[i - max_length: i + 1] == s[i - max_length: i + 1][::-1]:
                start = i - max_length
                max_length += 1
        return s[start: start + max_length]

    # 中心扩展法
    def longestPalindrome3(self, s):
        if not s:
            return s
        if len(s) == 1:
            return s
        result = s[0]
        maxl = 1
        for i in range(1, len(s)):
            # 先从字符向左右扩展。记录一下最多能扩展多少层
            extendl = min(i, len(s) - 1 - i)
            if extendl >= 1:
                for j in range(1, extendl + 1):
                    if s[i - j] == s[i + j]:
                        if j * 2 + 1 > maxl:
                            result = s[i - j:i + j + 1]  # 因为切片最后一个是不取的
                            maxl = j * 2 + 1
                    else:
                        break
            # 再从中间空隙扩展。记录能扩展多少层
            extendm = min(i, len(s) - i)
            for k in range(1, extendm + 1):
                if s[i - k] == s[i + k - 1]:
                    if k * 2 > maxl:
                        result = s[i - k:i + k]
                        maxl = k * 2
                else:
                    break
        return result

    # Manacher算法
    def longestPalindrome4(self, s):
        s = '#' + '#'.join(s) + '#'
        # RL[i]以第i个字符为中心的回文字串长度
        RL = [0] * len(s)
        # 当前扫描过的所有的回文串扩展到的最右边界
        MaxRight = 0
        # 扩展到最右边界的回文串的中间位置
        pos = 0
        # 最长回文长度
        MaxLen = 0
        MaxPos = 0
        for i in range(len(s)):
            if i < MaxRight:
                RL[i] = min(RL[2 * pos - i], MaxRight - i)
            else:
                RL[i] = 1
            # 尝试扩展，注意处理边界
            while i - RL[i] >= 0 and i + RL[i] < len(s) and s[i - RL[i]] == s[i + RL[i]]:
                RL[i] += 1
            # 更新MaxRight,pos
            if RL[i] + i - 1 > MaxRight:
                MaxRight = RL[i] + i - 1
                pos = i
            # 更新最长回文串的长度
            if RL[i] > MaxLen:
                MaxLen = RL[i]
                MaxPos = i
        return s[MaxPos - MaxLen + 1: MaxPos + MaxLen].replace('#', '')  # 去掉填充符号返回


if __name__ == '__main__':
    str_test = "abccbadd"
    print(Solution().longestPalindrome4(str_test))
