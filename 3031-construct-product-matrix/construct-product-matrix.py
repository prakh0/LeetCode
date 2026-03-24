class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])
        p = [[0] * m for _ in range(n)]
        mod = 12345
        suffix = 1
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                p[i][j] = suffix
                suffix = (suffix * grid[i][j]) % mod
        prefix = 1
        for x in range(n):
            for y in range(m):
                p[x][y] = (p[x][y] * prefix) % mod
                prefix = (prefix * grid[x][y]) % mod
        return p