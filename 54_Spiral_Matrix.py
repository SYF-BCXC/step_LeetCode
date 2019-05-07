#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 54_Spiral_Matrix
# @Author  : TCY
# @Time    : 2019/5/7 14:20
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        方法一. 右下左上的顺序，同时用一个vis矩阵记录是否访问过。
        方法二. 每次取一行，取完后旋转数组
        """
        """list的extend和+=效果一样，append是加整个list，extend和+=则是把元素丢进来。
        a = [1,2,3]
        a += [4,5,6]
        a.extend([7,8,9])
        a
        Out[22]: [1, 2, 3, 4, 5, 6, 7, 8, 9]

        zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的对象
        a = [[1,2,3],[4,5,6],[7,8,9]]
        list(zip(*a))
        Out[17]: [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
        最常用的：
        矩阵转置: list(map(list,zip(*a)))
        矩阵逆时针旋转(转置+行逆序): list(map(list,zip(*a)))[::-1]
        矩阵顺时针旋转(行逆序+转置)：list(map(list,zip(*a[::-1])))
        """
        ans = []
        while matrix:
            ans.extend(matrix.pop(0))
            if not matrix or not matrix[0]:
                return ans
            matrix[:] = list(map(list, zip(*matrix)))[::-1]
        return ans
        """ 方法1
        if not matrix:
            return []
        m, n = len(matrix), len(matrix[0])
        vis = [[False for _ in range(n)] for _ in range(m)]
        vis[0][0] = True
        x, y = 0, 0
        dx = [0,1,0,-1]
        dy = [1,0,-1,0]
        d = 0
        ans = [matrix[0][0]]
        while True:
            tx, ty = x+dx[d], y+dy[d]
            if not (0<=tx<m and 0<=ty<n and vis[tx][ty]==False):
                d = (d+1)%4
                tx,ty = x + dx[d], y+ dy[d]
                if not (0<=tx<m and 0<=ty<n and vis[tx][ty]==False):
                    return ans
            ans.append(matrix[tx][ty])
            vis[tx][ty] = True
            x, y = tx, ty
        """
