class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        seen = [False] * len(nums)
        result = []
        for num in nums:
            if seen[num] == True:
                result.append(num)
            else:
                seen[num] = True
        return result