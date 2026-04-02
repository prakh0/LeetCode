class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m = len(coins)
        n = len(coins[0])
        dp = [[[-float('inf')] * 3 for _ in range(n)] for _ in range(m)]

        if coins[0][0] >= 0:
            dp[0][0][0] = coins[0][0]
        else:
            dp[0][0][0] = coins[0][0]
            dp[0][0][1] = 0
        for i in range(m):
            for j in range(n):
                for k in range(3):
                    if dp[i][j][k] == -float('inf'):
                        continue
                    for di,dj in [(1,0), (0,1)]:
                        vi,vj = i + di, j + dj
                        if vi >= m or vj >= n:
                            continue
                        val = coins[vi][vj]
                        dp[vi][vj][k] = max(dp[vi][vj][k], dp[i][j][k] + val)
                        if val < 0 and k < 2:
                            dp[vi][vj][k+1] = max(dp[vi][vj][k+1], dp[i][j][k])
        result = max(dp[m-1][n-1])
        return result 