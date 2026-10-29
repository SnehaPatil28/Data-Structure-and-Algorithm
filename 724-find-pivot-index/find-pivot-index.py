class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        right_sum = sum(nums[1:len(nums)])
        left_sum = 0

        if left_sum == right_sum:
            return 0
        
        for i in range(len(nums)-1):
            left_sum = sum(nums[:i+1])
            right_sum = sum(nums[i+2:len(nums)])
         
            if left_sum == right_sum:
                return i+1

        return -1