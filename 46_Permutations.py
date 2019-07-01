"""
全排列
1、用回溯法
回溯可以有两种思考的方法。
- 一：每次从arr种抽取一个元素添加到tmp中
- 二：每次找元素i和当前元素交换
2、python一句话
list(itertools.permutations(nums))

"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        def helper(arr, tmp):
            if not arr:
                ans.append(tmp)
                return
            else:
                for i in range(len(arr)):
                    helper(arr[:i] + arr[i+1:], tmp + [arr[i]])
                    
        helper(nums, [])
        return ans
        


# 回溯法2
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        def helper(first):
            if first == n:
                ans.append(nums[:])
            else:
                for i in range(first, n):
                    nums[first], nums[i] = nums[i], nums[first]
                    helper(first+1)
                    nums[first], nums[i] = nums[i], nums[first]
        
        n = len(nums)
        helper(0)
        return ans
        
        