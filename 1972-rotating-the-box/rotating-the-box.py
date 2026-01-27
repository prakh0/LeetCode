class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m, n = len(box), len(box[0])
        for row in box:
            empty_space = len(row) - 1
            for i in range(len(row)-1,-1,-1):
                if row[i] == '*':
                    empty_space = i-1
                elif row[i] == '#':
                    row[i], row[empty_space] = '.', '#'
                    empty_space -= 1
        rotated_box = [[''] * m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                rotated_box[j][m - 1 - i] = box[i][j]
        return rotated_box 