class Solution:
    def isValidColumn(self, matrix, col):
        allowed = {'1','2','3','4','5','6','7','8','9'}
        for i in range(9):
            val = matrix[i][col]
            if val in allowed:
                allowed.discard(val)
            elif val == '.':
                pass
            else:
                return False
        return True

    def isValidRow(self, matrix, row):
        allowed = {'1','2','3','4','5','6','7','8','9'}
        for i in range(9):
            val = matrix[row][i]
            if val in allowed:
                allowed.discard(val)
            elif val == '.':
                pass
            else:
                return False
        return True

    def isValidCell(self, matrix, x, y):
        allowed = {'1','2','3','4','5','6','7','8','9'}
        for i in range(x*3,(x+1)*3):
            for j in range(y*3,(y+1)*3):
                val = matrix[i][j]
                if val in allowed:
                    allowed.discard(val)
                elif val == '.':
                    pass
                else:
                    return False
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for value in range(9):
            if self.isValidColumn(board, value) and self.isValidRow(board, value):
                pass
            else:
                return False

        for i in range(3):
            for j in range(3):
                if self.isValidCell(board, i, j):
                    pass
                else:
                    return False
        return True

# EOF #
