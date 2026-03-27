class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m, n = len(mat), len(mat[0])
        k = k % n 
        for i in range(m):
            original = mat[i]
            if i % 2 == 0:
                rotated = original[k:] + original[:k]
            else:
                rotated = original[-k:] + original[:-k]
            if rotated != original:
                return False
        return True