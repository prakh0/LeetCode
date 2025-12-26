class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = self.find_start(nums, target)         
        
        if start >= len(nums) or nums[start] != target:
            return[-1, -1]
        
        end = self.find_end(nums, target)
        
        return [start, end]

    def find_end(self, nums, target):
        start = 0
        end =len(nums)-1

        while start <= end:
            mid = (start + end)//2
            mid_val = nums[mid]

            if mid_val <= target:
                start = mid+1
            else:
                end = mid-1    
        
        return end            
    
    def find_start(self, nums, target):
        start = 0
        end = len(nums)-1 
        
        while start <= end:
            mid = (start + end)//2
            mid_val = nums[mid]
            
            if target <= mid_val:
                end = mid-1
            else:
                start = mid+1
                
        return start