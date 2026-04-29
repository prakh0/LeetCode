class Solution:
    def resultsArray(self, nums: list[int], k: int) -> list[int]:
        ans = []
        n = len(nums)

        for i in range(n - k + 1):
            is_consecutive = True
            max_val = nums[i]

            for j in range(i, i + k - 1):
                if nums[j] + 1 != nums[j + 1]:
                    is_consecutive = False
                    break
                max_val = max(max_val, nums[j + 1])

            ans.append(max_val if is_consecutive else -1)

        return ans