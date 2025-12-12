class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        result = sum(nums) % k
        return result