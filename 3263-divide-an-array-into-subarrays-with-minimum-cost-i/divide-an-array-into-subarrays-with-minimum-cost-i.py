class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        base = nums[0]
        first = float('inf')
        second = float('inf')
        j = 1
        for i in range(1,len(nums)):
            if nums[i] < first:
                second = first
                first = nums[i]
            elif nums[i] < second:
                second = nums[i]
        return base + first + second