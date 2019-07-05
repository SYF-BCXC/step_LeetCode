#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 840_Magic_Squares_In_Grid
# @Author  : TCY
# @Time    : 2019/7/5 16:02
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm

''' list按行，按列求和
>>> s=array([[1, 2, 3], [0, 0, 1], [1, 0, 1], [0, 1, 0]])
>>> s
array([[1, 2, 3],
       [0, 0, 1],
       [1, 0, 1],
       [0, 1, 0]])
>>> lin = map(sum,s)..........................在行方向上求和
>>> lin
[6, 1, 2, 1]
>>> col = map(sum,zip(*s))....................在列方向上求和
>>> col
[2, 3, 5]
'''


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def isMagic(arr):
            print(arr)
            dig1 = arr[0][0] + arr[1][1] + arr[2][2]
            dig2 = arr[0][2] + arr[1][1] + arr[2][0]
            hang = map(lambda x: sum(x), arr)
            lie = map(lambda x: sum(x), zip(*arr))
            s1 = set(hang) | set(lie)
            s1.add(dig1)
            s1.add(dig2)
            s2 = set(arr[0]) | set(arr[1]) | set(arr[2])
            s3 = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
            s2 = s2 & s3
            if len(s1) <= 1 and len(s2) == 9:
                return True
            else:
                return False

        if not grid: return 0
        n, m = len(grid), len(grid[0])
        if n < 3 or m < 3:
            return 0
        ans = 0
        for i in range(n - 2):
            for j in range(m - 2):
                if isMagic([grid[k][j:j + 3] for k in range(i, i + 3)]):
                    ans += 1
        return ans
