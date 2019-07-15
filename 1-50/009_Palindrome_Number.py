#!/usr/bin/python3

# @Project = leetCode
# @File    : 9_Palindrome_Number
# @Author  : TCY
# @Time    : 2018/9/24 15:19
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm

"""
题目描述:
https://leetcode-cn.com/problems/palindrome-number/description/
思路:
此题类似于第七题Reverse_Integer，思路同样可以参考
1、转换成string，然后[::-1]，这里多一个符号的处理
2、利用除法，获取不同位上的值
"""


"""c++

class Solution {
public:
    bool isPalindrome(int x) {
        if(x < 0 || (x % 10 == 0 && x != 0)) {
            return false;
        }

        int revertedNumber = 0;
        while(x > revertedNumber) {
            revertedNumber = revertedNumber * 10 + x % 10;
            x /= 10;
        }

        // 当数字长度为奇数时，我们可以通过 revertedNumber/10 去除处于中位的数字。
        // 例如，当输入为 12321 时，在 while 循环的末尾我们可以得到 x = 12，revertedNumber = 123，
        // 由于处于中位的数字不影响回文（它总是与自己相等），所以我们可以简单地将其去除。
        return x == revertedNumber || x == revertedNumber/10;
    }
};

"""


class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        s = str(x)
        s_r = s[::-1]
        if s_r == s:
            return True
        else:
            return False


if __name__ == '__main__':
    print(Solution().isPalindrome(101))
