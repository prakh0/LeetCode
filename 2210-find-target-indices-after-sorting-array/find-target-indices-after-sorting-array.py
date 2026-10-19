class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        smaller_target = 0
        target_count = 0
        for num in nums:
            if num < target:
                smaller_target += 1
            elif num == target:
                target_count += 1
        return list(range(smaller_target,smaller_target + target_count))