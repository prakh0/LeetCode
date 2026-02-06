class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        balanced_array = 0
        for right in range(len(nums)):
            while nums[right] >  k * nums[left]:
                left += 1
            balanced_array = max(balanced_array, right - left + 1)
        return len(nums) - balanced_array