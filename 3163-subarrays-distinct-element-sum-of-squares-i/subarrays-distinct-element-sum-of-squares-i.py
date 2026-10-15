class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        distinct_sum = 0
        for i in range(len(nums)):
            distinct = set()
            for j in range(i,len(nums)):
                distinct.add(nums[j])
                distinct_count = len(distinct)
                distinct_sum += distinct_count * distinct_count
        return distinct_sum