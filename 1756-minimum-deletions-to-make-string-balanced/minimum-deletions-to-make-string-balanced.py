class Solution:
    def minimumDeletions(self, s: str) -> int:
        count_b = delete = 0
        for i in s:
            if i == "b":
                count_b += 1
            elif count_b:
                delete += 1
                count_b -= 1
        return delete