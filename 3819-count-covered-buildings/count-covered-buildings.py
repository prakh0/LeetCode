class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        minRow = [n + 1] * (n+1)
        maxRow = [0] * (n+1)
        minCol = [n+1] * (n+1)
        maxCol = [0] * (n+1)

        for x,y in buildings:
            minRow[y] = min(minRow[y],x)
            maxRow[y] = max(maxRow[y],x)

            minCol[x] = min(minCol[x],y) 
            maxCol[x] = max(maxCol[x],y) 
        covered = 0
        for x,y in buildings:
            if minRow[y] < x < maxRow[y] and minCol[x] < y < maxCol[x]:
                covered +=1
        return covered