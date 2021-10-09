import math

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if row[0] <= target <= row[-1]:
                for val in row:
                    if val == target:
                        return True
                    else:
                        pass
            else:
                pass
        return False

# EOF #
# Esto era mejorable evitando hacer un ciclo for y tratando cada lista \
# como un bst aprovechando el ordenamiento.
