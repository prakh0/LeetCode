class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_jump = 0
        for i in range(len(nums)):
            if max_jump < 0:
                return False
            elif i > max_jump:
                return False
            else:
                max_jump = max(max_jump,nums[i]+i)
            if max_jump >= len(nums) -1:
                return True
        return False