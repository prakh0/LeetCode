class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def possible(speed):
            hours = 0
            for pile in piles:
                hours += (pile + speed - 1) // speed
            return hours <= h
    
        left, right = 1, max(piles)
    
        while left < right:
            mid = left + (right - left) // 2
            if possible(mid):
                right = mid
            else:
                left = mid + 1
    
        return left