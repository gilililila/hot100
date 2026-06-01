from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        将矩阵顺时针旋转 90° <=> 矩阵转置 + 水平反转
        矩阵转置 => 左上右下对角线反转 => matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        水平反转 => matrix[i].reverse()

        expansion:
        矩阵基础操作：水平反转-上下 H，垂直反转-左右 V，转置-主对角线 T
        对于矩阵 row * col
        H => arr[i][j] = arr[i][col-j-1] or arr[i].reverse()
        V => arr[i][j] = arr[row-i-1][j]
        T => arr[i][j] = arr[j][i]
        顺时针旋转90° => T+H
        逆时针旋转90° => T+V
        旋转180° => H+V
        按照副对角线转置 => T+H+V
        """
        n = len(matrix)
        for i, row in enumerate(matrix):
            for j in range(i+1, n):
                row[j], matrix[j][i] = matrix[j][i], row[j]
            row.reverse()

test_cases = [
    [[1,2,3],[4,5,6],[7,8,9]],
    [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
]

for case in test_cases:
    s = Solution()
    s.rotate(case)
    print(case)
