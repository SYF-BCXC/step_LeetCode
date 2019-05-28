#!/usr/bin/python3

# @Project = step_LeetCode
# @File    : 40_Combination_Sum_II
# @Author  : TCY
# @Time    : 2019/5/22 22:44
# @Email   : tangcaiyuan@hust.edu.cn
# @Software: PyCharm


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """回溯法尝试
        1. 每个元素或者不选，和大于target则剪枝
        注意事项：
        1.满足条件的不能return，这样会少一次pop操作导致出问题。
        2.set不能存list,dict,set，因为这些是可变的无法hash，存list只能存tuple
        3.sorted操作能够减少很多不必要的麻烦，因为大小有序，不会出现[1,1,6]和[1,6,1]这种重复答案的情况。
        """
        """
        n = len(candidates)
        candidates = sorted(candidates)
        def generate(i,tar,s,item,ans,res_set):
            if i>=n or s > tar:
                return
            item.append(candidates[i])
            s += candidates[i]
            if s == tar and tuple(item) not in res_set:
                ans.append(item[:])
                res_set.add(tuple(item))
            generate(i+1,tar,s,item,ans,res_set)
            item.pop()
            s -= candidates[i]
            generate(i+1,tar,s,item,ans,res_set)
        it = []
        an = []
        generate(0,target,0,it,an,set())
        return an
        """
        """回溯法的优化：
        1. 利用Python的特性，target不用传
        2. 再加入剪枝(从1440ms降低到了88ms)。candidates[i]>target则返回，或者选择了i之后超过了也返回
        """
        n = len(candidates)
        candidates = sorted(candidates)
        ans = []

        def helper(i, tar, item):
            if i >= n or tar < 0:
                return
            if candidates[i] > target:
                return
            if tar - candidates[i] < 0:
                return
            item.append(candidates[i])
            tar -= candidates[i]
            if tar == 0 and item not in ans:
                ans.append(item[:])
            helper(i + 1, tar, item)
            item.pop()
            tar += candidates[i]
            helper(i + 1, tar, item)

        helper(0, target, [])
        return ans


"""最快解答
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        if min(candidates) > target:
            return []
        n = len(candidates)
        res = []
        candidates.sort()
        def helper(idx, target, tem):
            if target == 0:
                res.append(tem)
                return
            if target < 0:
                return
            for i in range(idx, n):
                if candidates[i] > target:
                    break
                if i > idx and candidates[i]==candidates[i-1]:
                    continue
                helper(i+1, target-candidates[i], tem+[candidates[i]])
        helper(0, target, [])
        return res
"""
