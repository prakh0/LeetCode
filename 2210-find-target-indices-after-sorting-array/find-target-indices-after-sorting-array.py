class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        result = []
        for i in range(len(nums)):
            if nums[i] < target:
                continue
            if nums[i] == target:
                result.append(i)
            else:
                break
        return result