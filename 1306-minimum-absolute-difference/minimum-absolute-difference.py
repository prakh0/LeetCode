class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = float("inf")
        for i in range(len(arr)-1):
            min_diff = min(min_diff,arr[i+1] - arr[i])
        result = []
        for j in range(len(arr) -1):
            if arr[j+1] - arr[j] == min_diff:
                result.append([arr[j],arr[j+1]])
        return result