#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 1049_Last_Stone_Weight_II
# @Author  : TCY
# @Time    : 2019/5/27 16:48
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm

# 完全没有思路的一个题，贪心好像不太对，构造又不会，也不是数据结构题，搜索也用不上，递归回溯也不行，也不是动态规划，瞪着题直到比赛结束。。。

"""
本质上是一个为每个数配置正负号的问题。[a,b,c] 先选a和b碰撞, a-b(0则丢弃), 再把差值与c碰撞，即c-(a-b)，最后剩下的即为-a+b+c。
方法1：回溯(python超时,C++未测试)
方法2：利用bitset
"""

"""通过的C++版本的bitset

#include <bitset>
using namespace std;

const int bound = 40000;
const int capacity = 80000;

class Solution {
public:
    int lastStoneWeightII(vector<int>& stones) {
        // 用bitset
        bitset<80000> F;
        F.reset();
        F[bound] = 1;
        
        for (int stone: stones){
            F = (F << stone) | (F >> stone);
        }
        
        for (int i = bound; i < capacity; i++){
            if(F[i] == 1) return i-bound;
        }
        return -1;
    }
};
"""








class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        """本质是每个数配一个正负号的问题，总共有2^n种情况
        python bitset需要自己设计，用list感觉太慢；用10进制和2进制转换也不方便；因此用Bitset的方法还是用C++写比较好。
        这里用回溯法。(最后还是超时)
        回溯法最重要的就是在于剪枝。前面的值为负且绝对值已经超过后面的和则剪；前面的值的和大于总和的一半剪枝；另外如果和后面的和正好为0则直接返回0;
        """
        """计算i到最后一个元素的和"""
        aftSum = list(map(lambda x: sum(stones[x:]), range(len(stones))))
        n = len(stones)
        self.flag = False
        self.ans = 0xfffffff

        def helper(loc, tmp):
            if not 0 <= loc < n:
                return

            if abs(tmp) == abs(aftSum[loc]):
                self.flag = True
            if self.flag:
                self.ans = 0
                return

            if loc == n - 1:
                if tmp + stones[loc] >= 0:
                    self.ans = min(self.ans, tmp + stones[loc])
                if tmp - stones[loc] >= 0:
                    self.ans = min(self.ans, tmp - stones[loc])
                return

            tmp += stones[loc]
            if tmp > 0 and tmp <= aftSum[0]:
                helper(loc + 1, tmp)
            tmp = tmp - 2 * stones[loc]
            if tmp < 0 and abs(tmp) < aftSum[loc + 1]:
                helper(loc + 1, tmp)

        helper(0, 0)
        return self.ans

        '''bitset的尝试
        bound = 40000
        bitset = '0'*bound + '1' + '0'*bound
        bitset = int(bitset,2)
        for i in range(len(stones)):
            bitset = (bitset << stones[i]) | (bitset >> stones[i])
        bitset = bin(bitset)[2:]
        """转回2进制的时候前面的0会丢弃"""
        for i in range(len(bitset)-bound-1,len(bitset)):
            if bitset[i] == '1':return i
        return -1
        '''


