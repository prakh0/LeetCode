class Solution:
    def rotate(self,s:str, n:int) -> str:
        if not s:  
            return s
        n = n % len(s)
        return s[-n:] + s[:-n]
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        result = s
        visited = set()
        queue = deque([])
        queue.append(s)
        visited.add(s)
        while queue:
            current = queue[0]
            queue.popleft()
            if current < result:
                result = current
            temp = list(current)
            for i in range(1,len(temp),2):
                temp[i] = str((int(temp[i]) + a) % 10)
            temp_str = "".join(temp)
            if temp_str not in visited:
                visited.add(temp_str)
                queue.append(temp_str)

            rotated = self.rotate(current,b)
            if rotated not in visited:
                visited.add(rotated)
                queue.append(rotated)
        return result