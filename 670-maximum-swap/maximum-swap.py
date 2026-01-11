class Solution:
    def maximumSwap(self, num: int) -> int:
        nums =list(str(num))
        max_num = "0"
        max_i = -1
        swap_i = swap_j = -1

        for i in range(len(nums)-1,-1,-1):
            if nums[i] > max_num:
                max_num = nums[i]
                max_i = i

            if max_num > nums[i]:
                swap_i,swap_j = i, max_i

        nums[swap_i],nums[swap_j] = nums[swap_j],nums[swap_i]
        return int("".join(nums))