class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = {}
        for x in nums:
            if x in count:
                count[x] += 1
            else:
                count[x] = 1
        for x, freq in count.items():
            if freq == 1:
                return x
        return -1