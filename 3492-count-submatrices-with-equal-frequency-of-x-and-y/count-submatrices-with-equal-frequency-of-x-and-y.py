class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        currX = [[0] * col for _ in range(row)]
        currY = [[0] * col for _ in range(row)]
        count = 0
        for i in range(row):
            for j in range(col):

                currX[i][j] = 1 if grid[i][j] == 'X' else 0
                currY[i][j] = 1 if grid[i][j] == 'Y' else 0

                if i - 1 >= 0:
                    currX[i][j] += currX[i-1][j]
                    currY[i][j] += currY[i-1][j]

                if j - 1 >= 0:
                    currX[i][j] += currX[i][j-1]
                    currY[i][j] += currY[i][j-1]

                if i - 1 >= 0 and j - 1 >= 0:
                    currX[i][j] -= currX[i-1][j-1]
                    currY[i][j] -= currY[i-1][j-1]

                if currX[i][j] == currY[i][j] and currX[i][j] > 0:
                    count += 1
        return count