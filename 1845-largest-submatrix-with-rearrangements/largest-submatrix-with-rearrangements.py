class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        row = len(matrix)
        col = len(matrix[0])
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 1 and i > 0:
                    matrix[i][j] += matrix[i-1][j]
        max_area = 0
        for rows in matrix:
            rows.sort(reverse = True)
            for y in range(col):
                area = ((y + 1) * rows[y])
                max_area = max(max_area,area)
        return max_area