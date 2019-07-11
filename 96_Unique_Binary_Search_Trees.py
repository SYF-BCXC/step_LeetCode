#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 96_Unique_Binary_Search_Trees
# @Author  : TCY
# @Time    : 2019/7/10 10:27
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm

"""cpp
class Solution {
public:
    int numTrees(int n) {
        vector<int> dp(n+1,0);
        dp[0] = 1; dp[1] = 1;
        for(int i = 2; i <= n; i++){
            for (int j = 1; j<=i; j++){
                dp[i] += dp[j-1]*dp[i-j];
            }
        }
        return dp[n];
    }
};
"""