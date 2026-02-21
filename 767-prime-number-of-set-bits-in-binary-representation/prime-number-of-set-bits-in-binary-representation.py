class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        primes = {2,3,5,7,11,13,17,19}
        def countBitSet(n):
            count = 0
            while n:
                n = n & (n-1)
                count += 1
            return count
        result = 0
        for i in range(left,right+1):
            if countBitSet(i) in primes:
                result += 1
        return result
