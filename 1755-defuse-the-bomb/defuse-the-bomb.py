class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        result = [0]* len(code)
        if k == 0:
            return result
        for i in range(len(code)):
            total = 0
            if k > 0:
                for j in range(1,k+1):
                    total += code[(i + j) % len(code)]
            elif k < 0:
                for j in range(1,abs(k)+1):
                    total += code[(i - j) % len(code)]
            result[i] = total
        return result