class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        result = 0
        power = 1
        while n > 0:
            bit = n % 2
            masked = 1 - bit
            result += masked * power
            power *= 2
            n //= 2
        return result