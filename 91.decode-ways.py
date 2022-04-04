#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
    
        if not s:
            return 0
        
        # Let dp[ i ] = the number of ways to parse the string s[1: i + 1]
        # For example s = "231"
        # index 0: extra base offset. dp[0] = 1
        # index 1: # of ways to parse "2" => dp[1] = 1
        # index 2: # of ways to parse "23" => "2" and "23", dp[2] = 2
        # index 3: # of ways to parse "231" => "2 3 1" and "23 1" => dp[3] = 2

        N=len(s)
        dp = [0 for x in range(N + 1)] 

        # base case initialization
        dp[0] = 1 
        dp[1] = 0 if s[0] == "0" else 1   #(1) 1 way to decode 1 character

        for i in range(2, N+1): 
            # One step jump
            if 0 < int(s[i-1:i]) <= 9:    #(2) 
                dp[i] += dp[i-1]
            # Two step jump
            if 10 <= int(s[i-2:i]) <= 26: #(3)
                dp[i] += dp[i-2]
        return dp[N]
        
    
        
# @lc code=end

