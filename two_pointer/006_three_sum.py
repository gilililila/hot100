from typing import List

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """
        三数之和，可以转化为两数之和等于第三数
        题目要求和为0，将数组排序后，当前数大于0则和一定大于0
        遍历列表，把当前数当成第三数，其余两数在剩下的列表中使用双指针查找
        若和小于0，说明左指针太小，左指针右移，考虑到可能有重复的数，所以跳过所有重复值
        若和大于0，说明右指针太大，同理右指针左移
        只有和等于0时，记录当前的三数，然后左右指针同时移动，记得跳过重复值
        """
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            slow, fast = i + 1, len(nums) - 1
            while slow < fast:
                sum = nums[i] + nums[slow] + nums[fast]
                if sum < 0:
                    slow += 1
                    while slow < fast and nums[slow] == nums[slow - 1]:
                        slow += 1
                if sum > 0:
                    fast -= 1
                    while slow < fast and nums[fast] == nums[fast + 1]:
                        fast -= 1
                if sum == 0:
                    res.append([nums[i], nums[slow], nums[fast]])
                    slow += 1
                    fast -= 1
                    while slow < fast and nums[slow] == nums[slow - 1]:
                        slow += 1
                    while slow < fast and nums[fast] == nums[fast + 1]:
                        fast -= 1
        return res

test_cases = [
    [-1,0,1,2,-1,-4],
    [0,1,1],
    [0,0,0]
]

for case in test_cases:
    s = Solution()
    print(s.threeSum(case))
