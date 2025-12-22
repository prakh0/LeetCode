class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        lo = 0
        hi = len(removable)-1

        while lo <= hi:
            mid = lo + (hi-lo)//2
            if self.isSubsequence(s, p, mid, removable):
                lo = mid + 1
            else:
                hi = mid - 1
        return lo

    
    def isSubsequence(self, s: str, p: str, mid: int, removable: List[int]):
        removed = set(removable[:mid + 1]) 
        j = 0
        for i in range(len(s)):
            if i in removed:
                continue
            if s[i] == p[j]:
                j += 1
            if j == len(p):
                return True
        return False