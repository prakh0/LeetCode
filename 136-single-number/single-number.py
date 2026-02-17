class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = []
        for num in nums:
            if num not in result:
                result.append(num)
            else:
                result.remove(num)
        return result[0]