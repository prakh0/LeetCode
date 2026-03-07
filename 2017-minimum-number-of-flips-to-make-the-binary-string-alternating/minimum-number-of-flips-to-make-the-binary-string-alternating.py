class Solution:
    def minFlips(self, s: str) -> int:
        s = s+s
        n = len(s) // 2
        left = 0
        diff1 = diff2 = 0
        result = float("inf")
        for right in range(len(s)):
            expected1 = '0' if right % 2 == 0 else '1'
            expected2 = '1' if right % 2 == 0 else '0'
            if s[right] != expected1:
                diff1 += 1
            if s[right] != expected2:
                diff2 += 1
            if right - left + 1 > n:
                expected1_left = '0' if left % 2 == 0 else '1'
                expected2_left = '1' if left % 2 == 0 else '0'
                if s[left] != expected1_left:
                    diff1 -= 1
                if s[left] != expected2_left:
                    diff2 -= 1
                left += 1
            if right - left + 1 == n:
                result = min(result,diff1,diff2)
        return result