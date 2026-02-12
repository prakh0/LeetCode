class Solution:
    def longestBalanced(self, s: str) -> int:
        result = 0
        for left in range(len(s)):
            count = [0] * 26
            unique = max_freq = 0
            for right in range(left,len(s)):
                s_num = ord(s[right]) - ord("a")
                if count[s_num] == 0:
                    unique += 1
                count[s_num] += 1
                max_freq = max(max_freq,count[s_num])
                length = right - left +1
                if max_freq * unique == length:
                    result = max(result , length)
        return result