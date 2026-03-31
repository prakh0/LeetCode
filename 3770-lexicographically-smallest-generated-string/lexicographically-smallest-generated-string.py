class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n = len(str1)
        m = len(str2)
        word = ["?"] * (n + m - 1)
        canChange = [False] * (n + m - 1)
        for i in range(n):
            if str1[i] == "T":
                for j in range(m):
                    if word[i+j] == "?" or word[i+j] == str2[j]:
                        word[i+j] = str2[j]
                    else:
                        return ""
        for x in range(m + n - 1):
            if word[x] == "?":
                word[x] = "a"
                canChange[x] = True
        for i in range(n):
            if str1[i] == "F":
                if "".join(word[i:i+m]) == str2:
                    success = False
                    for j in range(m-1,-1,-1):
                        if canChange[i+j]:
                            word[i+j] = "b"
                            success = True
                            break
                    if success == False:
                        return ""
        return ''.join(word)
