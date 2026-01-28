class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            total = 0
            for i in str(n):
                digit = int(i)
                sqa = digit ** 2
                total += sqa
            n = total
        return True
