from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False
        count = Counter(nums)

        if count.most_common(1)[0][1] > 1:
            return True
        else:
            return False


# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
#         return len(set(nums)) < len(nums)
            
        
