class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        result = 0
        non_equal = [nums[0]]
        for i in range(1,len(nums)):
            if nums[i-1] != nums[i]:
                non_equal.append(nums[i])

        for i in range(1,len(non_equal)-1):
            if non_equal[i] < non_equal[i+1] and non_equal[i] < non_equal[i-1]:
                result += 1
            elif non_equal[i] > non_equal[i+1] and non_equal[i] > non_equal[i-1]:
                result += 1
            else:
                continue
        return result