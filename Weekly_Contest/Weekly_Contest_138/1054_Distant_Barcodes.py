#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 1054_Distant_Barcodes
# @Author  : TCY
# @Time    : 2019/5/27 9:56
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm

from collections import Counter


class Solution:
    def rearrangeBarcodes(self, barcodes):
        """想歪了，不用太注意相邻元素是否相同，直接利用奇偶位置的性质把元素隔开
        先将原数组按照出现的次数排序，出现最多的放前面。[1, 1, 1, 1, 3, 3, 2, 2, 2] -> [1, 1, 1, 1, 2, 2, 2, 3, 3]      1出现4次放最前面，2出现3次，3出现2次
        随后，将前一半放入ans的偶数位置，其他值直接放入奇数位置即可分开
        [1, 1, 1, 1, 2, 2, 2, 3, 3] , len = 9 ,前一半为 9//2+1 = 5
        ans = [1, _, 1, _, 1, _, 1, _, 2]   # 先放前一半
        ans = [1, 2, 1, 2, 1, 3, 1, 3, 2]   # 再放后一半
        """
        c = Counter(barcodes)
        arr = sorted(c.items(), key=lambda x: x[1], reverse=True)
        n = len(barcodes)

        source = []
        for i in range(len(arr)):
            for j in range(arr[i][1]):
                source.append(arr[i][0])

        ans = [0 for _ in range(n)]
        for i in range(n):
            # print(i)
            if i <= ((n + 1) // 2 - 1):
                # print(i*2)
                ans[i * 2] = source[i]
            else:
                # print((i-((n+1)//2-1)-1)*2+1)
                ans[(i - ((n + 1) // 2 - 1) - 1) * 2 + 1] = source[i]

        return ans


'''比赛时的思路    """dict + 回溯法"""
        count = {}
        ans = []
        n = len(barcodes)
        for i in range(n):
            if barcodes[i] in count:
                count[barcodes[i]] += 1
            else:
                count[barcodes[i]] = 1
        """还是贪心,超时"""
        k = list(count.keys())
        aa = 0
        while aa < n:
            """每次只插入一个值"""
            for i in k:
                flag = False
                if count[i] <= 0:
                    continue
                if not ans:
                    ans.append(i)
                    count[i] -= 1
                    flag = True
                else:
                    for j in range(len(ans)+1):
                        if j == 0:
                            if ans[j] != i:
                                ans.insert(j,i)
                                count[i] -= 1
                                flag = True
                                break
                        elif j == len(ans):
                            if ans[j-1] != i:
                                ans.insert(j,i)
                                count[i] -= 1
                                flag = True
                                break
                        else:
                            if ans[j]!=i and ans[j-1]!=i:
                                ans.insert(j,i)
                                count[i] -= 1
                                flag = True
                                break
                if flag:
                    break
            aa += 1
        return ans'''
'''        """开始回溯并注意剪枝"""
        def helper(c,a):
            if len(a) == n:
                return
            for i in c.keys():
                if (c[i] > 0 and not a) or (c[i]>0 and a and a[-1] != i):
                    """这个元素还能放"""
                    """放"""
                    c[i] -= 1
                    a.append(i)
                    helper(c,a)
                    """不放"""
                    c[i] += 1
                    a.pop()
                    helper(c,a)
        helper(count,ans)'''

'''第一名大佬的写法
import heapq
from collections import Counter


class Solution(object):
    def rearrangeBarcodes(self, barcodes):
        """
        :type barcodes: List[int]
        :rtype: List[int]
        """
        pq = []
        cnts = Counter(barcodes)
        for key, val in cnts.items():
            heapq.heappush(pq, (-val, key))
        result = []
        while pq:
            _, num = heapq.heappop(pq)
            cnts[num] -= 1
            if not result:
                result.append(num)
            else:
                last = result[-1]
                result.append(num)
                if cnts[last]:
                    heapq.heappush(pq, (-cnts[last], last))
        return result
'''

s = Solution()
barcodes = [1, 1, 1, 1, 2, 2, 3, 3]
print(s.rearrangeBarcodes(barcodes))
