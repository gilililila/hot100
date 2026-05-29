from collections import defaultdict
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        对于字母异位词而言，所含的字母是相同的，只是位置不同，可以将字母顺序排列，作为字母异位词的标签；
        python中字符串是可迭代对象，可以使用sorted进行排序，这样获得了字母异位词的唯一标签；
        defaultdict 在访问不存在的键时，自动常见一个空列表
        """
        dct = defaultdict(list)
        for s in strs:
            sorted_s = "".join(sorted(s))
            dct[sorted_s].append(s)
        return list(dct.values())

testCases = [
    ["eat","tea","tan","ate","nat","bat"],
    [""],
    ["a"]
]

for case in testCases:
    s = Solution()
    print(s.groupAnagrams(case))
