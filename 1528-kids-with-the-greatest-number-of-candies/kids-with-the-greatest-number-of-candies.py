class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        max_candy = max(candies)
        result = []

        for i in candies:
            new_candy = i + extraCandies
            result.append(True if new_candy >= max_candy else False)
            
        return result