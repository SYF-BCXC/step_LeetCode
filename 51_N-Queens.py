#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 51_N-Queens
# @Author  : TCY
# @Time    : 2019/5/23 12:20
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """回溯法"""
        ans = []
        """[
        //solution1 
        [2,5,6...] i表示第i行,ans[0][i]表示i行放在哪个位置
        ]"""

        def helper(i, item):
            """i表示当前填的行，item表示当前找的解"""
            if i > n:
                return
            if i == n:
                ans.append(item[:])
            for j in range(n):
                """找可以放的位置j"""
                flag = True
                for k in range(i):
                    """看列和斜"""
                    if item[k] == j or abs(item[k] - j) == abs(k - i):
                        flag = False
                        break
                if flag:
                    helper(i + 1, item + [j])

        helper(0, [])
        res = []
        """最后构造一下答案格式"""
        for i in range(len(ans)):
            item = []
            for j in range(len(ans[i])):
                tmp = '.' * ans[i][j] + 'Q' + '.' * (n - ans[i][j] - 1)
                item.append(tmp[:])
            res.append(item[:])
        return res
