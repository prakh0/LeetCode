class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        result = []
        for hours in range(12):
            for minute in range(60):
                if self.countBits(hours) + self.countBits(minute) == turnedOn:
                    result.append(f"{hours}:{minute:02d}")
        return result

    def countBits(self,n):
        count = 0
        while n > 0:
            n = n & (n-1)
            count += 1
        return count

