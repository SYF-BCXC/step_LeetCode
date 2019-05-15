#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 5055_Robot_Bounded_In_Circle
# @Author  : TCY
# @Time    : 2019/5/14 16:50
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        """按照指令执行十次，如果没有回到过原点则返回False;
        其实完全不需要十次，每次执行一遍指令，如果回到了原点肯定是True；如果执行完后，方向不为上，其他方向的话也一定会回来；只有一直向一个方向才不会回来。
        """
        n = 0
        x, y = 0, 0
        d = 0  # 右转+1，左转-1
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        while n < 10:
            for i in range(len(instructions)):
                if instructions[i] == 'G':
                    x, y = x + dx[d], y + dy[d]
                elif instructions[i] == 'L':
                    d = (d + 4 - 1) % 4
                elif instructions[i] == 'R':
                    d = (d + 1) % 4
            if x == 0 and y == 0:
                return True
            n += 1
        return False

