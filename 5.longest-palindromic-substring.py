#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ''
        result_length = 0
        for idx in range(len(s)):
            left,right = idx,idx
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > result_length:
                    result = s[left:right + 1]
                    result_length = right - left + 1
                left -= 1
                right += 1
            left,right = idx,idx+1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > result_length:
                    result = s[left:right + 1]
                    result_length = right - left + 1
                left -= 1
                right += 1
        return result
# @lc code=end

