#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height) -> int:
        result = 0
        left, right = 0, len(height) - 1
        while left != right:
            if height[left] <= height[right]:
                if height[left] * (right - left) > result:
                    result = height[left] *  (right - left)
                left += 1
            if height[left] > height[right]:
                if height[right] * (right - left) > result:
                    result = height[right] *  (right - left)
                right -= 1
        return result
# @lc code=end
