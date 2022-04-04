#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from contextlib import nullcontext



class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) ->ListNode:
        answer = ListNode(0)
        body = answer
        carry=0 
        while l1 or l2:
            sum_val = (l1.val if l1 else 0)+(l2.val if l2 else 0) + carry
            carry = sum_val // 10
            body.next = ListNode(sum_val%10)
            body = body.next
            if l1!=None:
                l1 = l1.next
            if l2!=None:
                l2 = l2.next
        if carry>0:
            body.next = ListNode(carry) 
        return answer.next
        
# @lc code=end

