class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        if len(nums) < 4:
            return False
        state = 0
        i = 0
        while i < len(nums) - 1:
            if state == 0:
                if nums[i] < nums[i + 1]:
                    i += 1
                    continue
                elif nums[i] > nums[i + 1]:
                    if i == 0:
                        return False
                    state = 1
                else:
                    return False
            elif state == 1:
                if nums[i] > nums[i + 1]:
                    i += 1
                    continue
                elif nums[i] < nums[i + 1]:
                    if i == 1:
                        return False
                    state = 2
                else:
                    return False
            else:
                if nums[i] < nums[i + 1]:
                    i += 1
                else:
                    return False
            
        return state == 2 