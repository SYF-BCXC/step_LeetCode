#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 5042_Escape_a_Large_Maze
# @Author  : TCY
# @Time    : 2019/4/28 19:41
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm


class Solution(object):
    def isEscapePossible(self, blocked, source, target):
        """
        :type blocked: List[List[int]]
        :type source: List[int]
        :type target: List[int]
        :rtype: bool
        """
        for i in range(len(blocked)):
            blocked[i] = tuple(blocked[i])
        blocked = set(blocked)
        self.maxsiz = (len(blocked) / 2 + 1) * (len(blocked) / 2 + 1)

        def dfs(x, y):
            if x < 0 or y < 0 or x >= 1000000 or y >= 1000000 or (x, y) in blocked or (x, y) in visited:
                return
            visited.add((x, y))
            self.count += 1
            if self.count > self.maxsiz:
                self.flag = True
                return
            dfs(x - 1, y)
            if self.flag:
                return
            dfs(x + 1, y)
            if self.flag:
                return
            dfs(x, y - 1)
            if self.flag:
                return
            dfs(x, y + 1)
            if self.flag:
                return

        self.flag = False
        visited = set()
        self.count = 0
        dfs(source[0], source[1])
        if not self.flag:
            return False
        self.flag = False
        visited = set()
        self.count = 0
        dfs(target[0], target[1])
        # print self.count, self.maxsiz, self.flag
        if not self.flag:
            return False
        return True
