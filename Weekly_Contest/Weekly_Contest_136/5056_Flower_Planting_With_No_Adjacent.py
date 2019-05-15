#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 5056_Flower_Planting_With_No_Adjacent
# @Author  : TCY
# @Time    : 2019/5/14 16:49
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm


class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        """
        1. 获得邻接矩阵
        2. 初始化为0，然后从1-4开始填(由邻接矩阵限制)
        """
        p = []
        for i in range(N + 1):
            p.append([])
        for i in range(len(paths)):
            a, b = paths[i]
            p[a].append(b)
            p[b].append(a)
        ans = [0 for _ in range(N)]
        for i in range(1, N + 1):
            if not p[i]:
                ans[i - 1] = 1  # 无邻接直接为1
            else:
                tmp = [True for _ in range(5)]  # 四个颜色能涂哪个
                for j in range(len(p[i])):
                    """1-4开始填，由这些邻接值限定"""
                    tmp[ans[p[i][j] - 1]] = False
                for k in range(1, 5):
                    if tmp[k]:
                        ans[i - 1] = k
                        break
        return ans

