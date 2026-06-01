from typing import List

DIRS = (0,1), (1,0), (0,-1), (-1,0)
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        row_num, col_num = len(matrix), len(matrix[0])
        total = row_num * col_num
        i, j, di = 0, -1, 0
        while len(res) < total:
            dx, dy = DIRS[di]
            for k in range(col_num):
                i += dx
                j += dy
                res.append(matrix[i][j])
            di = (di + 1) % 4
            row_num, col_num = col_num, row_num - 1
        return res

test_cases = [
    [[1,2,3],[4,5,6],[7,8,9]],
    [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
]

for case in test_cases:
    s = Solution()
    print(s.spiralOrder(case))
