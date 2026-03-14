class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        result = []
        count = [0]
        chars = ['a', 'b', 'c']
        def dfs(path):
            if len(path) == n:
                count[0] += 1
                if count[0] == k:
                    result.append(path)
                return
            for char in chars:
                if not path or path[-1] != char:
                    dfs(path + char)
                if result:
                    return
        dfs("")
        return result[0] if result else ""