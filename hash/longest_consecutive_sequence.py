from collections import defaultdict
from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        题目要求时间复杂度为 O(n)，说明不能排序，因为排序时间复杂度为 O(n*logn);
        为了去除重复元素，将列表转为无序、可变、元素唯一的集合 set；
        不断查找 n+1, n+2, ... 并计数，求得全局最大
        """
        h = set(nums)
        count = 0
        for n in h: # 遍历哈希集合
            if n - 1 in h: # 如果出现了小于当前数字的数，说明当前数字不是序列的开头，所以跳过；
                continue
            m = n + 1
            while m in h: # 不断查找 下一个数 是否存在于集合中；当循环退出时，m-1则是序列中最大的数
                m += 1
            count = max(count, m - n) # 从 n 到 m-1 一共有 m-n 个数
        return count

testCases = [
    [100,4,200,1,3,2],
    [0,3,7,2,5,8,4,6,0,1],
    [1,0,1,2]
]

for case in testCases:
    s = Solution()
    print(s.longestConsecutive(case))
