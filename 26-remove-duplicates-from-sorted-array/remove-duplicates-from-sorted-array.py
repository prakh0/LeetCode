class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        X=1
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[X] = nums[i]
                X += 1
        return X        