#include <string>
#include <iostream>
using namespace std;

class Solution {
public:
    vector<string> split(string s){
        vector<string> ans;
        int pos = 0;
        s.push_back(' ');
        for (int i = 0; i < s.length(); i++){
            if (s[i] == ' '){
                ans.push_back(s.substr(pos,i-pos));
                pos = i + 1;
            }
        }
        return ans;
    }
    bool wordPattern(string pattern, string str) {
        vector<string> words = split(str); // 写的熟练，注意切分时别带上空格
        map<char,string> m;
        if (pattern.length() != words.size()) return false;
        for (int i = 0; i < pattern.length(); i++){
            if (m.find(pattern[i]) != m.end()){ // 还可以通过compare函数进行比较
                // 该模式字母已经出现过，因此要求当前单词必须一模一样,如果不一样则返回false
                if(words[i] != m[pattern[i]]){
                    cout << "haveShow:"<< m[pattern[i]] << words[i] <<endl;
                    return false;
                }
            }
            else{
                // 该模式字母并未出现，要求当前单词必须与当前模式字母不同的单词不一样
                for (map<char,string>::iterator it = m.begin(); it != m.end(); it++){
                    if ( words[i] == it->second){
                        cout << "notShow:"<< it->second << " " << words[i] <<endl;
                        return false;
                    }
                }
                m[pattern[i]] = words[i];
            }
        }
        return true;
    }
};