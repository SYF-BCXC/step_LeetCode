#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 155_Min_Stack
# @Author  : TCY
# @Time    : 2019/5/1 22:01
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm

"""
最小值也用栈存虽然可以，但是内存利用率不高，存差值才是最好的
"""

class MinStack:
    # stack中存放实际值和最小值的差值
    # 压入或弹出负值时，最小值发生变化
    # 压入的总是栈顶减当前最小值，但是如果是负则更新最小值；压入的最小值正好作为更新最小值的flag
    # 弹出时，若为负数，则直接返回当前最小值，并更新得到最新的最小值；若>=0，则加上最小值返回
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min = 0
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if len(self.stack) == 0:
            self.min = x
            self.stack.append(0)
        else:
            self.stack.append(x - self.min)
            if x < self.min:
                self.min = x

    def pop(self):
        """
        :rtype: void
        """
        if len(self.stack) == 0:
            return

        x = self.stack.pop()
        if x < 0:
            self.min = self.min - x

    def top(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0:
            return
        x = self.stack[-1]
        if x > 0:
            return x + self.min
        else:
            return self.min

    def getMin(self):
        """
        :rtype: int
        """
        return self.min