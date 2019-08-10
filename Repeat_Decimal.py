#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : Repeat_Decimal
# @Author  : TCY
# @Time    : 2019/8/9 14:58
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm

"""寻找有理数的循环节。
a b -> c , 其中c = a / b，但是表示格式有限定
1 2  -> 0.5
1 3 -> 0.[3]
1 6 -> 0.1[6]
1 7 -> 0.[142857]

思路：
模拟手算过程，如果当前余数在前面出现过，则说明从其上一次出现位置到当前位置为循环节

由于输出过程中涉及'.'和'[]'这种多出来的符号，因此需要有标志位，表明是只有整数、整除但带小数、循环有理数

"""

a, b = map(int, input().split())

# 先获得整数部分
interger = a // b
remainder = (a % b) * 10
if remainder == 0:
    print(interger)
else:
    decimal = ''    # 小数部分
    index = 0       # 当前计算到第几位
    d = {}          # 记录是否出现以及出现时在第几位
    flag = True     # 记录是否有循环部分

    # 构造
    while remainder != 0:
        if remainder in d.keys():
            flag = False
            break
        else:
            d[remainder] = index
            div = remainder // b
            decimal += str(div)
            index += 1
            remainder = remainder % b * 10

    if flag:
        ans = str(interger) + '.' + decimal
    else:
        ans = str(interger) + '.' + decimal[:d[remainder]] + '[' + decimal[d[remainder]:index] + ']'
    print(ans)

