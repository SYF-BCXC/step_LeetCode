#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : test1
# @Author  : TCY
# @Time    : 2018/9/29 14:50
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm

class Solution:
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        N = len(board)

        def loc(num, n):
            a = n - (num // n) - 1
            if n % 2 == 0:
                if a % 2 == 0:
                    b = n - num % n
                else:
                    b = num % n - 1
            else:
                if a % 2 == 0:
                    b = num % n - 1
                else:
                    b = n - num % n
            return a, b



if __name__ == '__main__':
    print(Solution().snakesAndLadders([
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, 35, -1, -1, 13, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, 15, -1, -1, -1, -1]]))
