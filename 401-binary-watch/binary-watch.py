class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        result = []
        for hours in range(12):
            for min in range(60):
                if hours.bit_count() + min.bit_count() == turnedOn:
                    result.append(f"{hours}:{min:02d}")
        return result