
class Solution {
public:
    int numJewelsInStones(string J, string S) {
        vector<int> map(128,0);
        int ans = 0;
        for(int i=0; i<S.length(); i++){
            map[S[i]] ++;
        }
        for (int j=0; j<J.length(); j++){
            ans += map[J[j]];
        }
        return ans;
    }
};