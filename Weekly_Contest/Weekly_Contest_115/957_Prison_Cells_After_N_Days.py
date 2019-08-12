#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 957_Prison_Cells_After_N_Days
# @Author  : TCY
# @Time    : 2019/8/11 9:59
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm

class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        cells2 = [0 for _ in range(len(cells))]
        seen = {}
        while N > 0:
            ky = str(cells)
            seen[ky] = N

            for j in range(1, len(cells) - 1):
                if cells[j - 1] == cells[j + 1]:
                    cells2[j] = 1
                else:
                    cells2[j] = 0
            cells = cells2.copy()
            N -= 1

            ky = str(cells)
            if ky in seen:
                N %= (seen[ky] - N)
        return cells