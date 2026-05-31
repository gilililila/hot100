import collections
from typing import List


class Solution:
    def rotate1(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.

        先拼接两个相同的 nums 数组，此时我们注意到，所需的右旋转 k 步数组在这个大数组中，我们可以通过切片得到。
        由于我们是从左向右开始切片，等价于左旋转这个数组，也就是左旋转 len(nums)-k 步
        """
        l = len(nums)
        add_nums = nums + nums
        moves = k % l
        moves = l - moves
        nums[:] = add_nums[moves: moves + l]

    def rotate2(self, nums: List[int], k: int) -> None:
        """
        把一个子数组旋转两次，相当于没有变化。
        将数组分为两块 nums = A + B; 我们需要的旋转数组也就是 nums = B + A
        所以我们先将 nums 进行反转，得到 rev(B) + rev(A); 然后对各个部分进行反转，得到 B + A
        """
        def reverse(left: int, right: int) -> None:
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        l = len(nums)
        moves = k % l
        reverse(0, l - 1)
        reverse(0, moves - 1)
        reverse(moves, l - 1)

test_cases = [
    [[1,2,3,4,5,6,7], 3],
    [[-1,-100,3,99], 2]
]

for case in test_cases:
    s = Solution()
    s.rotate1(*case)
    print(case[0])

[1,2,3,4,5,6,7,1,2,3,4,5,6,7]
[-1,-100,3,99,-1,-100,3,99]
