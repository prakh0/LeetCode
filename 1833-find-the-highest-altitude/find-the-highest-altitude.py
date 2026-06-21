class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = 0
        result = 0
        for i in gain:
            altitude += i
            result = max(altitude,result)
        return result