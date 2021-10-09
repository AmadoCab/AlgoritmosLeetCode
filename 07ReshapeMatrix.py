class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        matrix = []
        if m*n == r*c:
            return [[mat[(c*i+j)//n][(c*i+j)%n] for j in range(c)] for i in range(r)]
        else:
            return mat

# EOF #
