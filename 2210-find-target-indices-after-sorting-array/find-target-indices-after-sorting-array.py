class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        lessCount = 0
        targetCount = 0
        for i in range(len(nums)):
            if nums[i] < target:
                lessCount += 1
            elif nums[i] == target:
                targetCount += 1
        return list(range(lessCount,lessCount + targetCount))