class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        index_map = {}
        for i,num in enumerate(nums):
            if nums[i]  in  index_map and abs(i-index_map[num]) <= k:
                    return True
            index_map[num] = i 
        return False