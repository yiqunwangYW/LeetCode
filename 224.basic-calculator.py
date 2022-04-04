#
# @lc app=leetcode id=224 lang=python3
#
# [224] Basic Calculator
#

# @lc code=start
class Solution:
    def calculate(self, s: str) -> int:
        res, num, sign, stack = 0,0,1,[]
        for ss in s:
            if ss in ['0','1','2','3','4','5','6','7','8','9']: # if ss.isdigit():
                num = num * 10 + int(ss)
            elif ss in ['+','-']:
                res += sign * num
                num = 0 
                #sign = [-1, 1][ss=='+']  
                sign = 1 if ss=='+' else -1
            elif ss =='(':
                stack.append(res)
                stack.append(sign)
                sign, res = 1, 0
            elif ss ==')':
                res += sign * num
                res *= stack.pop()
                res += stack.pop()
                num = 0
        return res + num * sign 



        
# @lc code=end

