class Solution:
    def lengthOfLIS(self, nums):
        """faster。关键在于抓住了最长上升的概念。每次找到该插入的位置时，如果不是最后面，则将该位置替换，这样会让序列尽可能的小"""
        def searchFB(arr, target):
            if not arr:
                return 0
            left, right = 0, len(arr)-1
            while left <= right:
                mid = left + ((right-left)>>1)
                if arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right + 1
        
        if not nums:
            return 0
        
        stack = [nums[0]]
        for i in range(1, len(nums)):
            loc = searchFB(stack, nums[i])
            if loc == len(stack):
                stack.append(nums[i])
            else:
                stack[loc] = nums[i]
        return len(stack)
        
                
    
    def lengthOfLIS_1(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [1 for _ in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i,-1, -1):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i],dp[j] + 1)
        return max(dp)