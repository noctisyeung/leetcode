#
# @lc app=leetcode id=1 lang=python
#
# [1] Two Sum
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # hash map to memorize the number in the we need with idx
        db_dict = {}
        result = []
        for idx, num in enumerate(nums):
            if (target - num) in db_dict:
                result = [db_dict[target - num], idx]
            else:
                db_dict[num] = idx
        return result
        
# @lc code=end

