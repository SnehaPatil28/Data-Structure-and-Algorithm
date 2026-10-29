class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        window_sum = sum(nums[:k])
        maxsum = window_sum
        
        for i in range(k, len(nums)):
            window_sum = window_sum - nums[i - k] + nums[i]
            maxsum = max(maxsum, window_sum)
        
        return maxsum / k