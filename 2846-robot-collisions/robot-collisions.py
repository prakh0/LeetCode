class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        indices = list(range(n))
        indices.sort(key = lambda i: positions[i])

        stack = []
        for current in indices:
            if directions[current] == 'R':
                stack.append(current)
            else:
                while stack and healths[current] > 0:
                    top = stack.pop()
                    if healths[current] > healths[top]:
                        healths[current] -= 1
                        healths[top] = 0
                    elif healths[current] < healths[top]:
                        healths[current] = 0
                        healths[top] -= 1
                        stack.append(top)
                    else:
                        healths[current] = 0
                        healths[top] = 0
        result = []
        for i in range(n):
            if healths[i] > 0:
                result.append(healths[i])
        return result