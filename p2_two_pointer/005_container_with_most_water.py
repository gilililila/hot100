from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
         计算最大长方形面积，而宽度与高度有矛盾，当宽度不断减小时，只有让高度增加才能遇到更大值
         为什么不会遗漏最优解，一方为较短柱时，当前的宽度时最大的，不论另一方怎么内缩，面积都小于当前面积，所以移动较短柱寻求更优解
         贪心+双指针结合
        """
        slow, fast = 0, len(height) - 1
        area = 0
        while slow < fast:
            h = min(height[slow], height[fast])
            area = max(area, h * (fast - slow))
            if height[slow] < height[fast]:
                slow += 1
            else:
                fast -= 1
        return area

test_cases = [
    [1,8,6,2,5,4,8,3,7],
    [1,2,1],
    [1,1]
]

for case in test_cases:
    s = Solution()
    print(s.maxArea(case))
