#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_len = 0
        right = 0

        set_table = set()

        for right ,_item in enumerate(s):
            while s[right] in set_table:
                set_table.remove(s[left])
                left = left + 1
            set_table.add(s[right])

            max_len = max(max_len, right - left + 1)

        return max_len
# @lc code=end
