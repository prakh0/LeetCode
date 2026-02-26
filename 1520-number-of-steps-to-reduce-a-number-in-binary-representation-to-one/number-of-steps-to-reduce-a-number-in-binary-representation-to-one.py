class Solution:
    def numSteps(self, s: str) -> int:
        steps = carry = 0 
        for i in range(len(s)-1,0,-1):
            bits = int(s[i])
            bits += carry
            if bits % 2 == 0:
                steps += 1
            else:
                steps += 2
                carry = 1
        return steps + carry 
