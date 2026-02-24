class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        char_count = {}
        for word in words:
            for char in word:
                if  char in char_count:
                    char_count[char] += 1
                else:
                    char_count[char] = 1
        for char in char_count:
            if char_count[char] % len(words):
                return False
        return True