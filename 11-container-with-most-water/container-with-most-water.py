class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_vol = 0
        i = 0
        j = len(height)-1
        while i < j:
            width = j-i
            depth = min(height[i],height[j])
            volume = width * depth
            max_vol = max(max_vol,volume)
            if height[i] < height[j]:
                i += 1
            elif height[i] > height[j]:
                j -= 1
            else:
                i += 1
                j -= 1
        return max_vol