""" https://leetcode.com/problems/binary-prefix-divisible-by-5/
update i on the fly and check if i is divisible by 5
""" 
from header import *

class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        ans = []
        x = 0
        for xx in A:
            x = (x<<1)+xx
            ans.append(x%5==0)
        return ans
        