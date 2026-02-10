class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        max_length = 0
        for i in range(len(nums)):
            even_num = set()
            odd_num  = set()
            for j in range(i,len(nums)):
                if nums[j] % 2 == 0:
                    even_num.add(nums[j])
                else:
                    odd_num.add(nums[j])
                if len(odd_num) ==len(even_num):
                    max_length = max(max_length, j - i + 1)
        return max_length