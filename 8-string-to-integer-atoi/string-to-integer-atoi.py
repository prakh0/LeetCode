class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s :
            return 0
        sign , i ,result = 1,0,0
        if i < len(s) and (s[i] == "-" or s[i] == "+"):
            if s[i] == "-":
                sign = -1
            i += 1
            
        while i < len(s) and  "0" <= s[i] <= '9':
            result = 10 * result + (ord(s[i]) - ord("0"))
            if result > (2**31 - 1):
                return sign * (2**31 - 1) if sign == 1 else -2**31
            i += 1
        return result * sign
