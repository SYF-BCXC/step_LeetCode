#include <map>
class Solution {
public:
    int longestPalindrome(string s) {
        int m[128] = {0};
        int ans = 0;
        int flag = 0;
        for (int i = 0; i < s.length(); i++){
            m[s[i]] ++;
        }
        for (int i = 0; i < 128; i++){
            if (m[i] % 2 == 1){
                ans += m[i]-1;
                flag = 1;
            }else{
                ans += m[i];
            }
        }
        ans += flag;
        return ans;
    }
};