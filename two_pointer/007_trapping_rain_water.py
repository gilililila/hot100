from sys import get_int_max_str_digits
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        """
        双向双指针，记录左、右的最高柱，通过左、右双向指针移动计算储水量
        选择左、右最高柱的较矮柱，是因为较矮柱决定了接下来的储水量
        """
        rain = left_max = right_max = 0 # 维护左、右最高柱
        left, right = 0, len(height) - 1
        # 双指针移动
        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            # 选择最高柱中的较矮柱一方进行移动，此时移动后的柱高差累加就是储水量
            if left_max < right_max:
                rain += left_max - height[left]
                left += 1
            else:
                rain += right_max - height[right]
                right -= 1
        return rain

    def trap2(self, height: List[int]) -> int:
        """
        单调栈，
        """
        ans = 0
        st = []
        for i, h in enumerate(height):
            while st and height[st[-1]] <= h:
                bottom_h = height[st.pop()]
                if not st:  # 栈是空的
                    break
                left = st[-1]
                dh = min(height[left], h) - bottom_h  # 面积的高
                ans += dh * (i - left - 1)
            st.append(i)
        return ans

    def trap3(self, height: List[int]) -> int:
        """
        动态规划，通过左右最高柱来计算当前柱是否能储水
        """
        rain = 0
        length = len(height)
        left_max = [0] * length
        right_max = [0] * length
        # 计算当前位置左边的最高柱
        left_max[0] = height[0]
        for i in range(1, length):
            left_max[i] = max(left_max[i - 1], height[i])
        # 计算当前位置右边的最高柱
        right_max[length - 1] = height[length - 1]
        for i in range(length - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])
        # 计算当前柱储水量
        for i in range(length):
            rain += min(left_max[i], right_max[i]) - height[i]

        return rain


test_cases = [
    [0,1,0,2,1,0,1,3,2,1,2,1],
    [4,2,0,3,2,5]
]

for case in test_cases:
    s = Solution()
    print(s.trap(case))

