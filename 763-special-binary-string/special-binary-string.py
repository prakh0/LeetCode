class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        count = 0 
        result = []
        start = 0
        for i in range(len(s)):
            if s[i] == '1':
                count += 1
            else:
                count -= 1
            if count == 0:
                s_string = self.makeLargestSpecial(s[start+1:i])
                result.append('1' + s_string + '0')
                start = i + 1
        result.sort(reverse = True)
        return "".join(result)