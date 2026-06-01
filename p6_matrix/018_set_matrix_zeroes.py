from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_has_zero = [0 in row for row in matrix]
        col_has_zero = [0 in col for col in zip(*matrix)]

        for i, r in enumerate(row_has_zero):
            for j, c in enumerate(col_has_zero):
                if r or c:
                    matrix[i][j] = 0

test_cases = [
    [[1,1,1],[1,0,1],[1,1,1]],
    [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
]

for case in test_cases:
    s = Solution()
    s.setZeroes(case)
    print(case)
