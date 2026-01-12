class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if  len(intervals) == 0:
            return []

        intervals.sort(key=lambda x: x[0])

        result = []
        prev = intervals[0]
        result.append(prev)

        for interval in intervals[1:]:
            if interval[0] <= prev[1]:
                prev[1] = max(interval[1], prev[1])
            else:
                prev = interval
                result.append(prev)

        return result
