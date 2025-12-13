class Solution:
    def maxSum(self, nums: List[int]) -> int:
        seen = set()
        result = 0
        max_element = float('-inf')
        for num in nums:
            max_element = max(max_element,num)
            if num > 0 and num not in seen:
                result += num
                seen.add(num)
        return result if result > 0 else max_element
