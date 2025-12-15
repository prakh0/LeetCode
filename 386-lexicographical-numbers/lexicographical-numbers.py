class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []
        current = 1
        for i in range(n):
            result.append(current)
            if current * 10 <=n:
                current *= 10
            else:
                while current == n or current % 10 == 9:
                    current //= 10 
                current += 1
        return result