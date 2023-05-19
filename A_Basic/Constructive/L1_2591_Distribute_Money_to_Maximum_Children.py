""" https://leetcode.com/problems/distribute-money-to-maximum-children/
Two cases will lead ans -= 1:
1. C==1 and M==3: only 1 child left and the child will receive 3 dollars
2. C==0 and M: no child left and the remained money will be assigned to any of the children
"""
class Solution:
    def distMoney(self, M: int, C: int) -> int:
        # Everyone must receive at least 1 dollar.
        M -= C
        if M<0: return -1
        # Find remained money and children
        ans = min(M//7, C)
        M -= 7*ans
        C -= ans
        # Two cases will lead ans -= 1
        if (C==1 and M==3) or (C==0 and M): 
            ans -= 1
        return ans