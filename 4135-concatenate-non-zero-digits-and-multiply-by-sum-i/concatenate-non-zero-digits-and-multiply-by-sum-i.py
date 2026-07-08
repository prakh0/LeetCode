class Solution:
    def sumAndMultiply(self, n: int) -> int:
        digits = []
        if n == 0:
            return 0
        while n > 0:
            digits.append(n % 10)
            n //= 10
        digits.reverse()
        x = 0
        digit_sum = 0
        for digit in digits:
            if digit != 0:
                x = x * 10 + digit
                digit_sum += digit
        return x * digit_sum