#
# @lc app=leetcode id=172 lang=python3
#
# [172] Factorial Trailing Zeroes
#

# @lc code=start
from mmap import PROT_WRITE

# Every trailing 0 is made by a factor of 5. Count the numbers in
# 1,...,n that are divisibe by 5, then those divisibe by 25
# which have a second factor of 5, then 125, etc...
# Time O(log n)
# Space O(1)


class Solution:
    # recursion
    # def trailingZeroes(self, n):
    #     if n<5:
    #         return 0
    #     else:
    #         return n//5 + self.trailingZeroes(n//5)

    def trailingZeroes(self, n):
        zeros, power_of_5 = 0,5
        while power_of_5 <=n:
            zeros +=n // power_of_5
            power_of_5 *= 5
        return zeros
        
    







        
# @lc code=end

