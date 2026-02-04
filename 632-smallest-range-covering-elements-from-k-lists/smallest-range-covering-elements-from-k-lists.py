class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        min_heap = []
        max_value = float('-inf')
        for i in range(len(nums)):
            heapq.heappush(min_heap, (nums[i][0], i, 0))
            max_value = max(max_value, nums[i][0])

        best_range = float('-inf'), float('inf')

        while min_heap:
            min_value, row, idx = heapq.heappop(min_heap)
            if max_value - min_value < best_range[1] - best_range[0]:
                best_range = min_value, max_value
            if idx + 1 == len(nums[row]):
                break
            next_value = nums[row][idx + 1]
            heapq.heappush(min_heap, (next_value, row, idx + 1))
            max_value = max(max_value, next_value)

        return list(best_range)