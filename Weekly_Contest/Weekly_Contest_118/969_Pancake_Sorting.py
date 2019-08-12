#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 969_Pancake_Sorting
# @Author  : TCY
# @Time    : 2019/8/12 15:02
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm


class Solution:
    """
    每次找到最大的数，将其先反转到第一个位置，再反转到它该在得位置
    [3,2,4,1]
    3,[4,2,3,1]
    4,[1,3,2,4]
    2,[3,1,2,4]
    3,[2,1,3,4]
    2,[1,2,3,4]
    """
    def pancakeSort(self, A: List[int]) -> List[int]:
        ans = []
        for cur in range(len(A), 0, -1):  # 从n到1
            loc = A.index(cur)
            ans.append(loc + 1)
            ans.append(cur)
            B = A.copy()
            for i in range(loc + 1):
                B[loc - i] = A[i]
            A = B.copy()
            for i in range(cur):
                B[cur - i - 1] = A[i]
            A = B.copy()
        return ans
