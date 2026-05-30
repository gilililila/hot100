import collections
import queue
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        window = collections.deque(maxlen=k)
        length = len(nums)
        for left, right in zip(range(1 - k, length - k + 1), range(length)):
            if left > 0 and window[0] == nums[left - 1]:
                window.popleft()
            while window and window[-1] < nums[right]:
                window.pop()
            window.append(nums[right])
            if left >= 0:
                res.append(window[0])
        return res

test_cases = [
    [[1,3,1,2,0,5], 3],
    [[7,2,4], 2]
]

for case in test_cases:
    s = Solution()
    print(s.maxSlidingWindow(*case))
