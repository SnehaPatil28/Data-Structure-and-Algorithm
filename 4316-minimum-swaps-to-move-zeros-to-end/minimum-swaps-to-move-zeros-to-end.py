class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        zero_count = 0
        swap = 0
        n = len(nums)

        for num in nums:
            if num == 0:
                zero_count += 1
        
        for i in range(n - zero_count, n):
            if nums[i] != 0:
                swap += 1
        
        return swap
        


        