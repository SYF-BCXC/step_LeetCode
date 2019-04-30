#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 1010_Pairs_of_Songs_With_Total_Durations_Divisible_by_60
# @Author  : TCY
# @Time    : 2019/4/30 13:51
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        """用dict保存出现的次数，若key_i 和 key_j 相加能被60整除，则加入 val_i * val_j"""
        """对于0和30要特殊处理"""
        co = {}
        for i in time:
            co[i % 60] = 1 if i % 60 not in co else co[i % 60] + 1
        """统计完成.能凑成60的 0+0 ,1+59, 2+58 ,..., 30+30
        对于a+a , 例co[a] = 4, C4选2
        对于a+b , 则直接 co[a] * co[b]
        """
        ans = 0
        if 0 in co:
            ans += co[0] * (co[0] - 1) // 2
        if 30 in co:
            ans += co[30] * (co[30] - 1) // 2
        for i in range(1, 30):
            if i in co and (60 - i) in co:
                ans += co[i] * co[60 - i]
        return ans
        """暴力超时
        n = len(time)
        ans = 0
        for i in range(n):
            for j in range(i,n):
                if i != j:
                    if (time[i] + time[j])%60 == 0:
                        ans += 1
        return ans
        """
