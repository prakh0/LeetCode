class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        result = [[0] * (n-k+1) for _ in range(m-k+1)]
        for i in range(m-k+1):
            for j in range(n-k+1):
                arr = []
                for x in range(i,i+k):
                    for y in range(j,j+k):
                        arr.append(grid[x][y])
                arr.sort()
                min_diff = float('inf')
                for z in range(1,len(arr)):
                    if arr[z] != arr[z-1]:
                        min_diff = min(min_diff, arr[z] - arr[z-1])
                result[i][j] = 0 if min_diff == float('inf') else min_diff
        return result