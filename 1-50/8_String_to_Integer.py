#!/usr/bin/python3

# @Project = leetCode
# @File    : 8_String_to_Integer
# @Author  : TCY
# @Time    : 2018/9/22 21:47
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm

"""
题目描述:
https://leetcode-cn.com/problems/string-to-integer-atoi/description/

思路:
1、先要找到第一个非空白字符。若其不为数字或者正负号，则直接返回0，结束。若为正负号或者数字，则一直扫描到不满足为之，因此会得到一串数字，将其转换为int。若超出32位int范围，则输出极限大小；否则，直接输出。结束。
2、直接先找到第一组数字区。判断前面是否为"多个空格一个符号"的形式，是，则继续；不是，则直接返回0。最后再是数字转换。

关于进制转换的补充：
1】 10进制转其他进制
bin(100)    #结果：'0b1100100'，类型为str
oct(100)    #结果：'0o144'，类型为str
hex(100)    #结果；'0x64',类型为str

2】 其他进制转10进制
int(str, 对应进制)
int('0x64',16)  #结果：100，类型int
int('0o144',8)  #结果：100，类型int

3】 关于最大值的问题
python3中，用sys.maxsize所得最大值为 9223372036854775807
此外，很有意思的事：
都知道32位int能表示的最小负数为-2147483648(2的31次方),最大正数为2147483647，绝对值中间差了1，是因为1000 0000 0000 0000 0000 0000 0000 0000 ，即-0，分配给了负数表示最小负数。
但是实际上，当我print(hex(-2147483648))的时候，答案并不是想象中的 0x80000000 ,而是-0x80000000
所以，在判断32位int能表示的范围的时候，在python中应该是，x >= -0x8000 0000 and x<= 0x7fff ffff

4】 Ascii码与字符之间的转换
ord('a')    # 结果为97，类型int
chr(65)     #结果为 'A'，类型为str
'A'     65
'Z'     90
'a'     97
'z'     122
'0'     48
'9'     57
"""


class Solution:
    # 此方法放弃，这个方法当遇到"-    123"时，应该输出0，但是会输出123。
    # 主要问题在于奇葩的情况太多，应该换种思路，直接把第一段数字先抠出来，如果前面不是"多个空格一个符号"的形式就返回0，可以减少大量判断的代码
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        start = 0
        stop = -1
        symbol_flag = 0  # 0表示正数，1表示负数
        flag = 0  # 0表示不在数字区，1表示在数字区
        flag2 = 0  # 未扫描过符号为0，扫描过为1；目的让双符号返回0
        # 先找第一个非空白符字符位置
        for x, z in enumerate(str):
            if z != ' ':
                # 可以用z.isdigit()代替
                if 57 >= ord(z) >= 48:
                    if stop < start:
                        # 第一次进入数字区
                        flag = 1
                        if str[x - 1] == '-':
                            symbol_flag = 1
                        start = x
                        stop = x
                    # 已经进入过数字区了
                    stop = x
                else:
                    # 不是数字的时候
                    if flag == 1:
                        # 已经经过数字区，结束循环
                        break
                    else:
                        # 没有经过数字区
                        if z == '+' or z == '-':
                            if flag2 == 0:
                                flag2 = 1
                            else:
                                return 0
                        else:
                            return 0
            else:
                if flag == 1:
                    break
        if flag == 0:
            return 0
        # 此时，将该数字转换出来
        my_num = int(str[start:stop + 1])
        if symbol_flag == 1:
            my_num = -my_num
        if my_num >= 0x7fffffff:
            my_num = 0x7fffffff
        if my_num <= -0x80000000:
            my_num = -0x80000000
        return my_num

    def myAtoi2(self, str):
        start = 0
        stop = -1
        symbol_flag = 0  # 0表示正数，1表示负数
        flag = 0  # 0表示不在数字区，1表示在数字区
        for x, z in enumerate(str):
            if 57 >= ord(z) >= 48:
                if stop < start:
                    # 第一次进入数字区
                    flag = 1
                    start = x
                    stop = x
                # 已经进入过数字区了
                stop = x
            else:
                if flag == 1:
                    break
        if start >= 1:
            if start >= 2:
                if not str[0:start-1].isspace():
                    return 0
            if str[start-1] != ' ':
                if str[start-1] != '+':
                    if str[start-1] == '-':
                        symbol_flag = 1
                    else:
                        return 0
        # 无法转换
        if flag == 0:
            return 0
        # 此时，将该数字转换出来
        my_num = int(str[start:stop + 1])
        if symbol_flag == 1:
            my_num = -my_num
        if my_num >= 0x7fffffff:
            my_num = 0x7fffffff
        if my_num <= -0x80000000:
            my_num = -0x80000000
        return my_num

    # 最快代码范例。用的就是思路2，但是不同在于设计了两个数组用于判定，速度快在不需要回头扫数字区前面的内容，一次扫描完成
    def myAtoi3(self, str):
        num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '+']
        k = len(str)
        for i in range(len(str)):
            if str[i] == ' ':
                continue
            if str[i] in nums:
                k = i
                break
            else:
                return 0
        e = len(str)
        for i in range(k + 1, len(str)):
            if str[i] in num:
                continue
            else:
                e = i
                break
        if str[k:e] == '-' or str[k:e] == '' or str[k:e] == '+':
            return 0
        r = int(str[k:e])
        INT_MIN = -pow(2, 31)
        INI_MAX = pow(2, 31) - 1
        if r < INT_MIN:
            return INT_MIN
        if r > INI_MAX:
            return INI_MAX
        return r


if __name__ == '__main__':
    print(Solution().myAtoi2("42"))
