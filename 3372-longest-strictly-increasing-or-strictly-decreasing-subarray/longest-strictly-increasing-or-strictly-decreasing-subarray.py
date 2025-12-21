class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        incr = decr = 1
        result = 1
        for i in range(1,len(nums)):
            if nums[i-1] < nums[i] :
                incr += 1
                decr = 1
            elif nums[i-1] > nums[i]:
                incr = 1
                decr += 1
            else:
                incr = 1
                decr = 1
            result = max(result,incr,decr)
        return result