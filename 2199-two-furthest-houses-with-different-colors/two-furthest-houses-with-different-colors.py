class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        result = 0
        for i in range(len(colors)):
            if colors[i] != colors[len(colors)-1]:
                result = max(result,len(colors) - 1 - i)
                break
        for j in range(len(colors)-1,-1,-1):
            if colors[j] != colors[0]:
                result = max(result, j)
                break
        return result 