class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lastWord = len(s.split()[-1])
        return lastWord