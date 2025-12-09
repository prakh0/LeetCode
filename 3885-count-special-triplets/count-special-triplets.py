class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        mod = 10**9 +7
        right = Counter(nums)
        left = Counter()
        result = 0
        for j in range(len(nums)):
            right[nums[j]] -= 1
            target = 2 * nums[j]
            result += left[target] * right[target]
            left[nums[j]] += 1
        return result % mod 