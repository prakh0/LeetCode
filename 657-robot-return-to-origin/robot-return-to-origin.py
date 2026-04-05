class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x = y = 0
        for ch in moves:
            if ch == 'U':
                x += 1
            elif ch == 'D':
                x -= 1
            elif ch == 'L':
                y += 1
            elif ch == 'R':
                y -= 1
        return x== 0 and y == 0