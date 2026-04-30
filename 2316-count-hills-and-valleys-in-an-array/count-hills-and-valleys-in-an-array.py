class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        arr = [nums[0]]
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                arr.append(nums[i])
        count = 0
        for j in range(1,len(arr) - 1):
            if arr[j] > arr[j-1] and arr[j] > arr[j+1]:
                count += 1
            elif arr[j] < arr[j-1] and arr[j] < arr[j+1]:
                count += 1
        return count