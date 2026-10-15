class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        current = 0
        max_sum = float("-inf")
        for num in nums:
            current += num
            max_sum = max(current,max_sum)
            if current < 0:
                current = 0
        return max_sum