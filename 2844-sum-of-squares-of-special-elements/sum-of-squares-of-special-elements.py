class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        result = 0
        for i in range(1,len(nums)+1):
            square_sum = 1
            if len(nums) % i   == 0:
                result += nums[i-1] * nums[i-1]
        return result