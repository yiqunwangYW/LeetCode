#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        for i, number in enumerate(nums):
            if target - number in res:
                return [res[target - number], i]
            res[number] = i
        return []
# @lc code=end

