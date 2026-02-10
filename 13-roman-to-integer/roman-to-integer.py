class Solution:
    def romanToInt(self, s: str) -> int:
        LS = { "I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000 }
        ans = 0
        for i in range(len(s)):
            if i + 1 < len(s) and LS[s[i]] < LS[s[i + 1]]:
                ans -= LS[s[i]]
            else:
                ans += LS[s[i]]  
        return  ans                