from typing import List


class Solution:
    def productExceptSelf1(self, nums: List[int]) -> List[int]:
        n = len(nums)

        pre_prod = [1] * n
        for i in range(1, n):
            pre_prod[i] = pre_prod[i - 1] * nums[i - 1]

        post_prod = [1] * n
        for j in range(n - 2, -1, -1):
            post_prod[j] = post_prod[j + 1] * nums[j + 1]

        res = [i * j for i, j in zip(pre_prod, post_prod)]

        return res

    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        for i in range(1, n):
            res[i] = res[i - 1] * nums[i - 1]

        post = 1
        for i in range(n - 1, -1, -1):
            res[i] *= post
            post *= nums[i]

        return res

test_cases = [
    [1,2,3,4],
    [-1,1,0,-3,3]
]

for case in test_cases:
    s = Solution()
    print(s.productExceptSelf2(case))
