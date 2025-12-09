class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        mod = 10**9 +7
        right = {}
        for x in nums:
            right[x] = right.get(x,0) + 1
        left = {}
        result = 0
        for j in range(len(nums)):
            right[nums[j]] -= 1
            target = 2 * nums[j]
            left_count = left.get(target,0)
            right_count = right.get(target,0)
            result = result + left_count*right_count
            left[nums[j]] = left.get(nums[j],0) + 1
        return result % mod 