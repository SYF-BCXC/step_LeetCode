#include<iostream>
using namespace std;
#include<map>
#include<vector>
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        // // ����һ�⡰ֻ����һ�ε����֡���Ŀ���ƣ������ȿ�����map�ɣ�û�����ִ�С��Χ����hash��̫���㣩
        // map<int,int> m;
        // for(int i=0;i<nums.size();i++){
        //     if(m.count(nums[i])){ //���߸�Ϊm.find(nums[i])!=m.end()
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
        // û�п�����Ŀ������һ����������ǳ���������
        // ��������������ͶƱ�Ļ��ƣ������˴��������������
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
