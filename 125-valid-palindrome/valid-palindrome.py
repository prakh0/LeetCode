class Solution:
    def isPalindrome(self, s: str) -> bool:
        left,right =0,len(s)-1
        while left < right:
            if s[left].isalnum() == False:
                left += 1 
            elif s[right].isalnum() == False:
                right -= 1
            elif s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                return False
        return True 