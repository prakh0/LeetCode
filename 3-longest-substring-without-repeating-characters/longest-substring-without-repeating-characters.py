class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        left = 0
        hash_set = {}
        for right in range(len(s)):
            if s[right] not in hash_set or hash_set[s[right]] < left:
                hash_set[s[right]] = right
                max_length = max(max_length,right - left + 1)
            else:
                left = hash_set[s[right]] + 1
                hash_set[s[right]] = right
        return max_length