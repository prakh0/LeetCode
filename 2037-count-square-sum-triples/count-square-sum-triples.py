class Solution:
    def countTriples(self, n: int) -> int:
        count = 0 
        for i in range(1,n-1):
            for j in range(i+1,n):
                c_sqr = i*i + j*j
                c = int(c_sqr ** 0.5)
                if c*c == c_sqr and c <= n:
                    count +=2
        return count 
