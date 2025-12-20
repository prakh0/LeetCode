class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        word = set(dictionary)
        memo = {}
        def recursion(i:int)->int:
            if i == len(s):
                return 0
            if i in memo:
                return memo[i]
            result = len(s) -i
            for j in range(i,len(s)):
                if s[i:j+1] in word:
                    result = min(result,recursion(j+1))
            result = min(result, 1 + recursion(i + 1))
            memo[i] = result
            return result
        return recursion(0)
