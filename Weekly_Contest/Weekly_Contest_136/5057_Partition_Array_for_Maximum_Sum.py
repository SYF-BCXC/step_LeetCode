#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 5057_Partition_Array_for_Maximum_Sum
# @Author  : TCY
# @Time    : 2019/5/14 16:48
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm

"""常见动态规划总结见棕色笔记本"""

import copy


class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        '''改进maxx初始化的问题'''
        n = len(A)
        if n == 0: return 0
        if n == 1: return A[0]
        dp = [0 for _ in range(n + 5)]
        """动态规划 dp[i] = max(dp[i-1]+maxx[i][i],dp[i-2]+2*maxx[i-1][i]...)"""
        for i in range(1, n + 1):
            curmax = 0
            for j in range(1, K + 1):
                if i - j >= 0:
                    curmax = max(curmax, A[i - j])
                    dp[i] = max(dp[i], dp[i - j] + j * curmax)
        return dp[n]
        '''超时了，可能在maxx初始化用时太多
        """所用变量与初始化"""
        n = len(A)
        maxx = [[0 for _ in range(n+5)]for _ in range(n+5)]
        dp = [0 for _ in range(n+5)]
        for i in range(1,n+1):
            for j in range(i,n+1):
                maxx[i][j] = max(A[i-1:j])
        """动态规划 dp[i] = max(dp[i-1]+maxx[i][i],dp[i-2]+2*maxx[i-1][i]...)"""
        for i in range(1,n+1):
            for j in range(1,K+1):
                if i-j >= 0:
                    dp[i] = max(dp[i],dp[i-j]+j*maxx[i-j+1][i])
        return dp[n]
        '''
        """ 每K个一组，计算每组的最大收益，然后贪心
        贪心算法不通过，部分解答不为最优！感觉类似于打家劫舍那个题，[5,7,6]，贪心为7，实际为5+6
        [20779,436849,274670,543359,569973,280711,252931,424084,361618,430777,136519,749292,933277,477067,502755,695743,413274,168693,368216,677201,198089,927218,633399,427645,317246,403380,908594,854847,157024,719715,336407,933488,599856,948361,765131,335089,522119,403981,866323,519161,109154,349141,764950,558613,692211]
26
ans:42389649
        """
        '''
        def get_max(arr,l,r):
            m = arr[l]
            while l <= r:
                if arr[l]>m:
                    m = arr[l]
                l += 1
            return m

        def assign(arr,l,r,m):
            while l<=r:
                arr[l] = m
                l+=1

        gain = {}
        for i in range(len(A)-K+1):
            m = get_max(A,i,i+K-1)
            g = 0
            for j in range(K):
                g += (m-A[i+j])
            gain[i] = g
        """ gain[i]表示[i:i+k]段的收益，用v记录已经被选取的部分,vis记录该段收益"""
        vis = copy.deepcopy(A)
        v = [False for _ in range(len(A))]
        # 当没有可能再选取一组个数为K的元素时候，结束
        while gain:
            max_gain_idx = max(gain,key=gain.get)
            m = get_max(A,max_gain_idx,max_gain_idx+K-1)
            for i in range(K):
                vis[max_gain_idx+i] = m
                v[max_gain_idx+i] = True
            # 删除周围有覆盖该部分段的其他gain
            for i in range(K):
                if max_gain_idx+i-K+1 >= 0 and (max_gain_idx+i-K+1) in gain:
                    gain.pop(max_gain_idx+i-K+1)
                if max_gain_idx+i < len(A) and (max_gain_idx+i) in gain:
                    gain.pop(max_gain_idx+i)
        # 最后将中间小于K个一组的，让其变成当前组最大
        after_process = []
        for i in range(len(v)):
            if (not v[i] and i > 0 and v[i-1]):
                after_process.append(i)
            if i==0 and not v[i]:
                after_process.append(i)
            if (not v[i] and i+1<len(v) and v[i+1]):
                after_process.append(i)
            if i == (len(v)-1) and not v[i]:
                after_process.append(i)
        while after_process:
            b = after_process.pop()
            a = after_process.pop()
            m = get_max(vis,a,b)
            while a<=b:
                vis[a] = m
                a += 1
        sum = 0
        for i in vis:
            sum += i
        return sum
        '''
