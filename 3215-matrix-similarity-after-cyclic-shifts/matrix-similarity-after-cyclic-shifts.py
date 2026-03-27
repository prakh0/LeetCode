class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m, n = len(mat), len(mat[0])
        k = k % n 
        if k == 0:
            return True
        for i in range(m):
            for j in range(n):
                if i % 2 == 0:
                    final = (j + k) % n
                else:
                    final = (j-k+n) % n
                if mat[i][j] != mat[i][final]:
                    return False
        return True
            
