from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        双指针法，慢指针用来定位，而快指针用来判断
        当快指针位置不为0时，应该将其插入慢指针位置，此时慢指针才移动
        快指针一直在检索，所以一直移动
        """
        slow, fast = 0, 0
        while fast < len(nums):
            if nums[fast]:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
            fast += 1

test_case = [
    [0,1,0,3,12],
    [0],
    [5,4,0,1,6,3]
]
for case in test_case:
    s = Solution()
    s.moveZeroes(case)
    print(case)
