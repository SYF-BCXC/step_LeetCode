#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 347_Top_K_Frequent_Elements
# @Author  : TCY
# @Time    : 2019/7/14 15:20
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm


from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        return heapq.nlargest(k,c.keys(), key=c.get)
"""        q = []
        for k,v in c.items():
            heapq.heappush(q,(v,k))
            if len(q) > k:
                heapq.heappop(q)
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(q)[1])
        ans.reverse()
        return ans"""

""" 不用堆，时间开销大
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        its = sorted(c.items(), key=lambda x: x[1], reverse=True)
        print(its)
        ans = []
        for i in range(k):
            ans.append(its[i][0])
        return ans
"""