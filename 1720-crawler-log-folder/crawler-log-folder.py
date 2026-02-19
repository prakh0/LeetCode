class Solution:
    def minOperations(self, logs: List[str]) -> int:
        result = 0
        for operation in logs:
            if operation == "./":
                continue
            elif operation == '../':
                if result > 0:
                    result -= 1
            else:
                result += 1
        return result