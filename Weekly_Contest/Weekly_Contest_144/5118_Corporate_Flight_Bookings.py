#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 5118_Corporate_Flight_Bookings
# @Author  : TCY
# @Time    : 2019/7/7 14:30
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm
"""

这里有 n 个航班，它们分别从 1 到 n 进行编号。

我们这儿有一份航班预订表，表中第 i 条预订记录 bookings[i] = [i, j, k] 意味着我们在从 i 到 j 的每个航班上预订了 k 个座位。

请你返回一个长度为 n 的数组 answer，按航班编号顺序返回每个航班上预订的座位数。



示例：

输入：bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5
输出：[10,55,45,25,25]


提示：

1 <= bookings.length <= 20000
1 <= bookings[i][0] <= bookings[i][1] <= n <= 20000
1 <= bookings[i][2] <= 10000
"""

"""
这个题非常赞。
一个区间[a,b]加c，等价于,全部元素加c再[b:]减c
"""

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res = [0 for _ in range(n + 1)]

        for update in bookings:
            start, end, inc = update[0] - 1, update[1] - 1, update[2]
            res[start] += inc
            res[end + 1] -= inc

        for i in range(1, n):
            res[i] += res[i - 1]

        return res[:-1]