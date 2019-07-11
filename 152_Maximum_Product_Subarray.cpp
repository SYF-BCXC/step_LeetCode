/*
维护一个最大值，一个最小值。
最大值 = max(最大值*当前值，最小值*当前值，当前值)
最小值 = min(最小值*当前值，最大值*当前值，当前值)
*/

#include <cmath>
class Solution {
public:
    int maxProduct(vector<int>& nums) {
        if (nums.size() == 0) return 0;
        int n = nums.size();
        int cur_max = nums[0], cur_min = nums[0], ans = nums[0];
        for (int i = 1; i < nums.size(); i++){
            int tmp = cur_max;
            cur_max = max(max(cur_max*nums[i], cur_min*nums[i]), nums[i]);
            cur_min = min(min(cur_min*nums[i], tmp*nums[i]), nums[i]);
            ans = max(cur_max, ans);
        }
        return ans;
    }
};