from typing import List, Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
        定长窗口移动，window是长度为len(p)的窗口；
        left表示当前窗口的左侧，当window中计数与p_count相同，left则为窗口起始下标
        """
        window = Counter()
        p_count = Counter(p)
        res = []
        for right, ch in enumerate(s):
            window[ch] += 1
            left = right - len(p) + 1
            if left < 0:
                continue
            if window == p_count:
                res.append(left)
            window[s[left]] -= 1
        return res

test_cases = [
    ["cbaebabacd", "abc"],
    ["abab", "ab"]
]

for case in test_cases:
    sol = Solution()
    print(sol.findAnagrams(case[0],case[1]))
