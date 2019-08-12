#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 974_Subarray_Sums_Divisible_by_K
# @Author  : TCY
# @Time    : 2019/8/12 11:14
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm


class Solution:
    """
    利用前缀和的思想。
    A = [4,5,0,-2,-3,1]
    prefix sum : [4,9,9,7,4,5]  正常来说获得sum(A[i+1:j+1]) = prefixSum[j] - prefixSum[i]
    我们现在要找sum(A[i:j+1]) % K == 0的所有序列，即(prefixSum[j] - prefixSum[i]) % K == 0
    因此，prefixSum[j] % K == prefixSum[i] % K, 这样从前往后，如果prefix sum%K在前面出现过，则sum(A[i+1:j+1])必定为K的倍数
    prefix sum%K:[4,4,4,2,4,0]
    第一个4，过；第二个4，ans+=1

    坑：为了便于hash，sm的值要限定在[0,K)之间，因为sm可能变为负数，在C++和java中余数可能依旧为负数，但是其实是和+K是等价的。(这里python除正数的时候向负无穷取整，因此正好余数会是正)
    """

    def subarraysDivByK(self, A: List[int], K: int) -> int:
        ans = 0
        sm = 0
        mp = {0: 1}
        for i in range(len(A)):
            sm = ((sm + A[i]) % K + K) % K
            if sm in mp:
                ans += mp[sm]
                mp[sm] += 1
            else:
                mp[sm] = 1
        return ans
