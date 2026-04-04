class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if rows == 0:
            return " "
        col = len(encodedText)// rows
        
        matrix = []
        index = 0
        for i in range(rows):
            row = []
            for j in range(col):
                row.append(encodedText[index])
                index += 1
            matrix.append(row)
        result = []
        for x in range(col):
            i,j = 0,x
            while i < rows and j < col:
                result.append(matrix[i][j])
                i += 1
                j += 1
        return "".join(result).rstrip()