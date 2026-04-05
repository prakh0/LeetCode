class Solution:
    def judgeCircle(self, moves: str) -> bool:
        freq = {}
        for ch in moves:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1
        if freq.get('U',0) == freq.get('D',0) and freq.get('L',0) == freq.get('R',0):
            return True
        return False