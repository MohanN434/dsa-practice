class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        R, C = len(matrix), len(matrix[0])
        self.sumMat = [[0] * (C + 1) for _ in range(R + 1)]

        for i in range(R):
            prefix = 0
            for j in range(C):
                prefix += matrix[i][j]
                above = self.sumMat[i][j + 1]
                self.sumMat[i + 1][j + 1] = prefix + above

        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1, c1, r2, c2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1

        top = self.sumMat[r1 - 1][c2]
        left = self.sumMat[r2][c1 - 1]
        topLeft = self.sumMat[r1 - 1][c1 - 1]
        current = self.sumMat[r2][c2]

        return current - left - top + topLeft

        