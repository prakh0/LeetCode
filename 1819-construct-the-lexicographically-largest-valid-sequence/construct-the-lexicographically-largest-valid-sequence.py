class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        result = [0]* (2*n-1) 
        used = [False] * (n+1)
        def backtracking(index):
            if index == len(result):
                return True
            if result[index] != 0:
                return backtracking(index+1)
            for i in range(n,0,-1):
                if used[i] == True:
                    continue
                if i == 1:
                    result[index] = 1
                    used[1] = True
                    if backtracking(index + 1):
                        return True
                    result[index] = 0
                    used[1] = False
                else:
                    j = index + i
                    if j < len(result) and result[j] == 0:
                        result[index] = result[j] = i
                        used[i] = True
                        if backtracking(index + 1):
                            return True
                        result[index] = result[j] = 0
                        used[i] = False
            return False

        backtracking(0)
        return result