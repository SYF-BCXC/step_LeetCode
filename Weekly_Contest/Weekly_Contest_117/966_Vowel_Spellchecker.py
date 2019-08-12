#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 966_Vowel_Spellchecker
# @Author  : TCY
# @Time    : 2019/8/11 20:55
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm


class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def tovowel(s):
            res = ''
            s = s.lower()
            vowel = ['a', 'e', 'i', 'o', 'u']
            for i in s:
                if i in vowel:
                    res += '#'
                else:
                    res += i
            return res

        origin = {}
        cap = {}
        vowel = {}

        for idx, val in enumerate(wordlist):
            if val not in origin:
                origin[val] = val
            if val.lower() not in cap:
                cap[val.lower()] = val
            if tovowel(val) not in vowel:
                vowel[tovowel(val)] = val

        ans = []
        for query in queries:
            if query in origin:
                ans.append(query)
            elif query.lower() in cap:
                ans.append(cap[query.lower()])
            elif tovowel(query) in vowel:
                ans.append(vowel[tovowel(query)])
            else:
                ans.append('')
        return ans


