class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set('aeiou')
        def is_valid_word(word: str) -> bool:
            return word[0] in vowels and word[-1] in vowels

        n = len(words)
        prefix = [0] * (n + 1)
        for i in range(n):
            if is_valid_word(words[i]):
                prefix[i + 1] = prefix[i] + 1  
            else:
                prefix[i + 1] = prefix[i] 
        result = []
        for lo, ro in queries:
                result.append(prefix[ro+1] - prefix[lo])
        return result
