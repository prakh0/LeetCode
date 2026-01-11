class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        sieve = [True] * (right + 1)
        sieve[0] = sieve[1] = False
        for i in range(2, int(right ** 0.5) + 1):
            if sieve[i] == True:
                for j in range(i * i, right + 1, i):
                    sieve[j] = False
        primes = []
        for i in range(left, right + 1):
             if sieve[i] == True:
                primes.append(i)
        
        if len(primes) < 2:
            return [-1, -1]
        min_diff = float("inf")
        result = [-1, -1]
        for i in range(1, len(primes)):
            diff = primes[i] - primes[i - 1]
            if diff < min_diff:
                min_diff = diff
                result = [primes[i - 1], primes[i]]

        return result