class Solution:
    def check(self,mid,mountainHeight,workerTimes) -> bool:
        height = 0
        for t in workerTimes:
            height += int(math.sqrt(2.0 * mid/t + 0.25) - 0.5)
            if height >= mountainHeight:
                return True
        return height >= mountainHeight
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        maxTime = max(workerTimes)
        left = 1 
        right = maxTime * mountainHeight * (mountainHeight + 1) // 2
        result = 0
        while left <= right:
            mid = left + (right - left) // 2
            if self.check(mid,mountainHeight,workerTimes):
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        return result