from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """ 遍历列表，同时查询字典；
        字典中存储nums的编号，if 永远查询当前编号之前的数；
        每种输出只会对应一个答案，若当前数没有答案，则出现覆盖后也不会有答案 """
        dct = {}
        for i, n in enumerate(nums):
            req = target - n
            if req in dct:
                return [dct[req], i]
            else:
                dct[n] = i

testCases = [
    [[2,7,11,15], 9],
    [[3,2,4], 6],
    [[3,3], 6]
]

for case in testCases:
    s = Solution()
    print(s.twoSum(*case))
