from math import floor
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        intervals.sort()
        res = []
        left, right = intervals[0][0], intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] > right:
                res.append([left, right])
                left, right = intervals[i][0], intervals[i][1]
            left = min(left, intervals[i][0])
            right = max(right, intervals[i][1])
        res.append([left, right])
        return res

test_cases = [
    [[1,3],[2,6],[8,10],[15,18]],
    [[1,4],[4,5]],
    [[4,7],[1,4]]
]

for case in test_cases:
    s = Solution()
    print(s.merge(case))
