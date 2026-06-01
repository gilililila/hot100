from typing import List

class Solution:
    def firstMissingPositive1(self, nums: List[int]) -> int:
        """
        不必多说
        时间复杂度 O(n)
        空间复杂度 O(n)
        """
        st = set(nums)
        res = 1
        while res in st:
            res += 1
        return res

    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        我们有一个 nums 数组，长度是 length，那么缺失的最小正数一定在 [1, length+1]内。
        当我们的数组中出现了一个大于数组长度的数，说明一定有一个大小介于 [1, length+1] 的数缺失。
        为了找到这样的数，我们首先遍历一次数组，尝试吧每个数字放到正确的位置，排序思路如下：
            当前数字 nums[i] 应该处于索引 nums[i]-1 处，如果索引处不是 nums[i]，则进行交换
            置换得来的数，我们进行同样的操作，所以使用while循环嵌套。
            对于超出数组长度的数，或者是已经排序的数，我们忽略。
        遍历排序好的数组，
            如果当前的数与下标不匹配，说明该下标应匹配的数为缺失的第一个正数。
            如果所有的数都匹配，说明该数组后一个数(length+1) 是缺失的第一个正数。

        时间复杂度 O(n) 每个元素最多被交换一次，while循环总执行次数为 n
        空间复杂度 O(1)
        """
        length = len(nums)

        for i in range(length):
            while 0 < nums[i] <= length and nums[nums[i] - 1] != nums[i]:
                pos = nums[i] - 1
                nums[i], nums[pos] = nums[pos], nums[i]

        for i in range(length):
            if nums[i] != (i + 1):
                return i + 1

        return length + 1

test_cases = [
    [1,2,0],
    [3,4,-1,1],
    [7,8,9,11,12]
]

for case in test_cases:
    s = Solution()
    print(s.firstMissingPositive(case))
