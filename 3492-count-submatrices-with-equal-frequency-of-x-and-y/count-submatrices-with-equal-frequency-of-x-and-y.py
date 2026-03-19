class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        currX = [0] * col 
        currY = [0] * col 
        count = 0
        for i in range(row):
            countX = 0
            countY = 0
            for j in range(col):
                if grid[i][j] == 'X':
                    currX[j] += 1

                elif grid[i][j] == 'Y':
                    currY[j] += 1
                countX += currX[j]
                countY += currY[j]
                if countX == countY and countX > 0:
                    count += 1
        return count