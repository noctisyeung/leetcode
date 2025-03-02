#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    """Class representing a solution to the problem."""

    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        sorted_list = sorted(nums)
        result_list = []
        max_length = 0
        for idx, num in enumerate(sorted_list):
            if idx == 0:
                max_length = 1
                result_list.append(num)
                continue
            if num - 1 == sorted_list[idx - 1]:
                result_list.append(num)
                max_length = len(result_list) if len(result_list) > max_length else max_length
            elif num == sorted_list[idx - 1]:
                # bypass same number
                continue
            else:
                max_length = len(result_list) if len(result_list) > max_length else max_length
                result_list = []
                result_list.append(num)
        return max_length
# @lc code=end

