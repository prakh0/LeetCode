class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        total = sum(nums)
        prefix = 0
        count = 0
        
        for i in range(len(nums)):
            if nums[i] == 0:
                L = prefix
                R = total - prefix - nums[i]
                
                diff = abs(L - R)
                
                if diff == 0:
                    count += 2
                elif diff == 1:
                    count += 1
            
            prefix += nums[i]
        
        return count
