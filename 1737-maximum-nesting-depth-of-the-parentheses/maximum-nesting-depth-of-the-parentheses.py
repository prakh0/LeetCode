class Solution:
    def maxDepth(self, s: str) -> int:
        result = 0
        depth = 0
        for i in s:
            if i == "(":
                depth += 1
                result = max(depth,result)
            elif i == ")":
                depth -= 1
        return result