#include<iostream>
using namespace std;
#include<map>
#include<vector>
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        // // û��˼·�����ø����ռ�,��map������,hashӦ��Ҳ����
        // map<int,int> m;
        // for(int i = 0;i<nums.size();i++){
        //     if(m.find(nums[i])->second){
        //         m[nums[i]]++;
        //     } else{
        //         m.insert(pair<int,int>(nums[i],1));
        //     }
        // }
        // for(map<int,int>::iterator it=m.begin();it!=m.end();++it){
        //     if(it->second == 1){
        //         return it->first;
        //     }
        // }
        // return -1;
        // �ٿ���һ�²��ø����ռ�ķ���,a^a=0
        int result = 0;
        for(int i = 0;i<nums.size();i++){
            result^=nums[i];
        }
        return result;
    }
};
