class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        N = len(matrix)
        M = len(matrix[0])
        left,right = 0 , M*N-1
        while left<=right:
            mid = (left + right)// 2
            i ,j = divmod(mid,M)
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                left = mid+1
            else:
                right = mid-1
        return False                