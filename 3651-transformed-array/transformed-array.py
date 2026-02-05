class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        for i in range(len(nums)):
            if nums[i] == 0:
                result[i] = nums[i]
            else:
                new_index = (i + nums[i]) % len(nums)
                result[i] = nums[new_index]
        return result
