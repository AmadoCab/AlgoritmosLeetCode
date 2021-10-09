class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1]]
        for i in range(1,numRows):
            row = []
            for j in range(i+1):
                if j == 0:
                    row.append(1)
                elif j == i:
                    row.append(1)
                else:
                    row.append(triangle[-1][j]+triangle[-1][j-1])
            triangle.append(row)
        return triangle

# EOF #
