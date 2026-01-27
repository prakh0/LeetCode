class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        num_min = min(nums)
        num_max = max(nums)
        result = []
        seen = set(nums)
        for i in range(num_min,num_max+1):
            if i not in seen:
                result.append(i)
        return result