class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = -1, 0
        max_len = 0
        dct = {}
        for right in range(len(s)):
            if s[right] in dct:
                left = max(dct[s[right]], left)
            dct[s[right]] = right
            max_len = max(max_len, right - left)
        return max_len

test_cases = [
    "abcabcbb",
    "bbbbb",
    "pwwkew"
]

for case in test_cases:
    s = Solution()
    print(s.lengthOfLongestSubstring(case))
