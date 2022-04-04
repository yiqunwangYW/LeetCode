#
# @lc app=leetcode id=442 lang=python3
#
# [442] Find All Duplicates in an Array
#

# @lc code=start
import collections

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dic = collections.Counter(nums)
        return [key for key in dic if dic[key]==2]
        
# @lc code=end

