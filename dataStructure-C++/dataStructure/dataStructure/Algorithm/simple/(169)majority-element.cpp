#include<iostream>
using namespace std;
#include<map>
#include<vector>
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        // // 和上一题“只出现一次的数字”题目类似，还是先考虑用map吧（没给数字大小范围，用hash不太方便）
        // map<int,int> m;
        // for(int i=0;i<nums.size();i++){
        //     if(m.count(nums[i])){ //或者改为m.find(nums[i])!=m.end()
        //         m[nums[i]]++;
        //     }else{
        //         m.insert(pair<int,int>(nums[i],1));
        //     }
        // }
        // int max = 0;
        // int result=0;
        // for(map<int,int>::iterator it=m.begin();it!=m.end();it++){
        //     if(max<(it->second)){
        //         result = it->first;
        //         max = it->second;
        //     }
        // }
        // return result;
        // 没有看清题目，大于一半的数，不是出现最多的数
        // 可以利用类似于投票的机制，让众人代表的数保存下来
        int same=nums[0],sum=0;
        for(int i=0;i<nums.size();i++){
            if(sum==0){
                same=nums[i];
            }
            if(same==nums[i]){
                sum++;
            }else{
                sum--;
            }
        }

        return same;
    }
};
