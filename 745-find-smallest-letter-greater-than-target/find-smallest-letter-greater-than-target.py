class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        t = ord(target)
        result = None
        for ch in letters:
            if ord(ch) > t:
                result = ch
                break
        return result if result is not None else letters[0]