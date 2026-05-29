from collections import defaultdict
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre_sum = [0] * (len(nums)+1)
        count = 0
        # 计算前缀和
        for i in range(len(nums)):
            pre_sum[i+1] = pre_sum[i] + nums[i]

        pre_count = defaultdict(int)
        for num in pre_sum:
            count += pre_count[num - k]
            pre_count[num] += 1

        return count

test_cases = [
    [[1,1,1], 2],
    [[1,2,3], 3],
    [[1,1,-1,1,-1], 1]
]

for case in test_cases:
    s = Solution()
    print(s.subarraySum(*case))
