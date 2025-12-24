class Solution(object):
    def minAddToMakeValid(self, s):
        stack = []
        result = 0
        for i in s:
            if i == "(":
                stack.append("(")
                result += 1
            elif stack and stack[-1] == "(" and i == ")":
                stack.pop()
                result -= 1
            else:
                result += 1
        return result