#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 973_K_Closest_Points_to_Origin
# @Author  : TCY
# @Time    : 2019/8/12 11:12
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        ans = sorted(points, key=lambda x: x[0] * x[0] + x[1] * x[1])
        return ans[:K]


"""        def getDis(point):
            return point[0]**2 + point[1]**2
        d = []
        ans = []
        for i in points:
            dis = getDis(i)
            loc = bisect.bisect(d, dis)
            d.insert(loc, dis)
            ans.insert(loc, i)
        return ans[:K]"""