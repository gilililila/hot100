import collections

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cnt_t = collections.Counter(t)
        kinds = len(cnt_t)
        req_k = 0
        ans_left, ans_right = -1, len(s)
        left = 0

        for right, ch in enumerate(s):
            cnt_t[ch] -= 1
            if cnt_t[ch] == 0:
                req_k += 1
            while req_k == kinds:
                if right - left < ans_right - ans_left:
                    ans_left, ans_right = left, right
                left_ch = s[left]
                if cnt_t[left_ch] == 0:
                    req_k -= 1
                cnt_t[left_ch] += 1
                left += 1
        return "" if ans_left < 0 else s[ans_left: ans_right + 1]

        # cnt_s = collections.Counter()
        # cnt_t = collections.Counter(t)
        #
        # left = 0
        # ans_left, ans_right = -1, len(s)
        #
        # for right, ch in enumerate(s):
        #     cnt_s[ch] += 1
        #     while cnt_s >= cnt_t:
        #         if right - left < ans_right - ans_left:
        #             ans_left, ans_right = left, right
        #         cnt_s[s[left]] -= 1
        #         left += 1
        # return "" if ans_left < 0 else s[ans_left: ans_right + 1]


test_cases = [
    ["ADOBECODEBANC", "ABC"],
    ["a", "a"],
    ["a", "aa"]
]

for case in test_cases:
    s = Solution()
    print(s.minWindow(*case))
