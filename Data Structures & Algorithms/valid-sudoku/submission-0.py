from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowMap, colMap, gridMap = defaultdict(set), defaultdict(set), defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue

                val = board[i][j]
                if (val in rowMap[i] or val in colMap[j] or val in gridMap[(i//3, j//3)]):
                    return False

                rowMap[i].add(val)
                colMap[j].add(val)
                gridMap[(i//3, j//3)].add(val)

        return True