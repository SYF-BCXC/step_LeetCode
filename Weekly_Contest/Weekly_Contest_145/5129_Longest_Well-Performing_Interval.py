#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 5129_Longest_Well-Performing_Interval
# @Author  : TCY
# @Time    : 2019/7/14 12:07
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm

"""
思路：1、滑动窗口。
2、A[i]+A[i+1]+...+A[j] 满足某条件，则(A[0]+A[1]+...+A[j]) - (A[0]+A[1]+...+A[i-1])也满足该条件。
"""

"""
下面尝试的方法都超时了，大体思路有了，但是在求最长的问题上还是没有很好的思路。
大佬AC代码：(除了上述方法外，用了二分的思想，但是maxn是什么？)
    int longestWPI(vector<int>& hours) {
        int a[10005],maxn[10005],i,j,n=hours.size();
        // 初始化数组a，a[i]代表[0,i)的转化和
        a[0]=0;	
        for (i=0;i<n;i++)
        {
            if (hours[i]>8) {
                a[i+1]=1;
            }else {
                a[i+1]=-1;
            }
            a[i+1]+=a[i];
        }
        maxn[n+1]=-100000000;
        for (i=n;i>=1;i--) maxn[i] = max(maxn[i+1],a[i]);
        int ans=0;
        for (i=1;i<=n;i++)
        {
            int tar=a[i-1];
            int l=i,r=n;
            while (l<=r)
            {
                int mid=(l+r)>>1;
                if (maxn[mid]>tar) {l=mid+1;}
                else {r=mid-1;}
            }
            ans=max(ans,r-i+1);
        }
        return ans;
    }
"""

class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        dp = [0 for _ in range(len(hours) + 1)]  # dp[i] 表示[0,i)的转化和
        for i in range(len(hours)):
            dp[i + 1] = dp[i] + 1 if hours[i] > 8 else dp[i] - 1

        n = len(hours)
        # 现在开始从最长的长度开始缩减找满足条件的第一个
        # dp[6] - dp[2] 代表[0,6) - [0,2)，即[2,6)或[2,5]

        # [0,6], (dp[7]-dp[0])
        # [0,5],[1,6], (dp[6]-dp[0],dp[7]-dp[1])
        # [0,4],[1,5],[2,6],
        for i in range(n, -1, -1):
            for j in range(0, n - i + 1, 1):
                if dp[j + i] - dp[j] > 0:
                    return i
        return 0


""" 单独找区间和等于1的最长子串不行,[9,9,9]
        cc = list(map(lambda x:1 if x>8 else -1, hours))
        dp = {0: -1}
        count = 0
        maxLen = 0
        for i in range(0, len(cc)):
            count = count + cc[i]
            if count not in dp:
                dp[count] = i
                if (count-1) in dp:
                    tmp = i - dp[count - 1]
                    maxLen = max(tmp,maxLen,count)
            else:
                if (count-1) in dp:
                    tmp = i - dp[count - 1]
                    maxLen = max(tmp,maxLen,count)
        return maxLen"""

""" 直接暴力无果
dp = [[0 for _ in range(len(hours))] for _ in range(len(hours))]
        ans = 0
        for i in range(len(hours)):
            for j in range(i, len(hours)):
                if j == i:
                    dp[i][j] = 1 if hours[i] > 8 else -1
                else:
                    if hours[j] > 8:
                        dp[i][j] = dp[i][j-1] + 1
                    else:
                        dp[i][j] = dp[i][j-1] - 1
                if dp[i][j] > 0 and j-i+1 > ans:
                    ans = j-i+1
        return ans"""
