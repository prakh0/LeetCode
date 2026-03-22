class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for _ in range(4):
            if mat == target:
                return True
            self.rotate(mat)
        return False
    def rotate(self,mat):
        for i in range(len(mat)):
            for j in range(i,len(mat)):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
        for row in mat:
            row.reverse()
    