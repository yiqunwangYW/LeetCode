#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start

# Notice that the solution set must not contain duplicate triplets.
# But triplet can contain duplicate element!!!

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        if len(nums)<3:
            return []

        nums.sort()
        N, result = len(nums), []

        for i in range(N):
            if i>0 and nums[i]==nums[i-1]:
                continue # prevent dups
            target = -1 * nums[i]

            l = i+1
            r = N-1
            while l < r:
                if nums[l]+nums[r] == target:
                    result.append([nums[i], nums[l], nums[r]])
                    l +=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1 # prevent dups
                elif nums[l]+nums[r] < target:
                    l +=1
                else:
                    r -=1
        return result

        
# @lc code=end

