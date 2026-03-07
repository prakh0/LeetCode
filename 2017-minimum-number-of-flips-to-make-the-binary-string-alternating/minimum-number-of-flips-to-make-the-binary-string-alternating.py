class Solution:
    def minFlips(self, s: str) -> int:
        s = s+s
        n = len(s) // 2
        left = right = 0
        diff1 = diff2 = 0
        result = float("inf")
        s1 = ['0' if i % 2 == 0 else '1' for i in range(len(s))]
        s2 = ['1' if i % 2 == 0 else '0' for i in range(len(s))]
        while right < len(s):
            if s[right] != s1[right]:
                diff1 += 1
            if s[right] != s2[right]:
                diff2 += 1
            if right - left + 1 > n:
                if s[left] != s1[left]:
                    diff1 -= 1
                if s[left] != s2[left]:
                    diff2 -= 1
                left += 1
            if right - left + 1 == n:
                result = min(result,diff1,diff2)
            right += 1
        return result