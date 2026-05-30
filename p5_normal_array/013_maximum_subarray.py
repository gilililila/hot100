from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        cur_sum = 0
        if len(nums) == 1:
            return nums[0]
        for i in range(len(nums)):
            if cur_sum < nums[i] and cur_sum < 0:
                cur_sum = nums[i]
            else:
                cur_sum += nums[i]
            max_sum = max(max_sum, cur_sum)
        return max_sum
        # if len(nums) == 1:
        #     return nums[0]
        # pre_sum = [0] * (len(nums) + 1)
        # for i in range(1, len(nums) + 1):
        #     pre_sum[i] = pre_sum[i - 1] + nums[i - 1]
        # print(pre_sum)
        # max_sum = float('-inf')
        # min_num = 0
        # for right in range(1, len(pre_sum)):
        #     max_sum = max(max_sum, pre_sum[right] - min_num)
        #     min_num = min(min_num, pre_sum[right])
        # return max_sum




test_cases = [
    [1,2],
    [-2,-1],
    [-2,1,-3,4,-1,2,1,-5,4],
    [1],
    [5,4,-1,7,8]
]

for case in test_cases:
    s = Solution()
    print(s.maxSubArray(case))
