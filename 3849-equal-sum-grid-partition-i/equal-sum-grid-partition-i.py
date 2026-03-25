class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        total = sum(sum(row) for row in grid)
        if total % 2 != 0:
            return False
        target = total // 2
        s = 0
        for i in range(m-1):
            s += sum(grid[i])
            if s == target:
                return True
        s = 0
        for j in range(n-1):
            s += sum(grid[i][j] for i in range(m))
            if s == target:
                return True
        return False
