#
# @lc app=leetcode id=1688 lang=python3
#
# [1688] Count of Matches in Tournament
#

# @lc code=start
class Solution:
    def numberOfMatches(self, n: int) -> int:
        if n==1:
            return 0
        elif n==2:
            return 1
        elif n%2:
            return n//2+self.numberOfMatches(1+n//2)
        else:
            return n//2+self.numberOfMatches(n//2)


        
# @lc code=end

