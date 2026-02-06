class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10**9 + 7
        result = {}

        def dfs(length):
            if length > high:
                return 0
            if length in result:
                return result[length]

            count = 1 if low <= length <= high else 0
            count += dfs(length + zero)
            count += dfs(length + one)
    
            result[length] = count % MOD
            return result[length]
        return dfs(0)