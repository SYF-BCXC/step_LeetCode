//
// Created by Dawn on 2019/3/22.
//

#include<iostream>
using namespace std;

class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        // 三个指针，两个分别指向数组最后一个元素，一个指针指向从后往前填的最后一个元素

        // 1. 初始化指针
        int flag = m + n - 1;
        int a = m - 1;
        int b = n - 1;
        // 2. 从后往前遍历，直到一个数组元素遍历结束，再将另外一个数组直接填入

    }
};

