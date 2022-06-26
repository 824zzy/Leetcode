""" https://leetcode.com/problems/maximum-xor-after-operations/
Inspiration: if there is "1" in i-th bit, the final result of i-th bit is '1'
"""
class Solution:
    def maximumXOR(self, A: List[int]) -> int:
        ans = 0
        for i in range(32):
            f = False
            for x in A:
                if (x>>i)&1: f = True
            if f: ans += 1<<i
        return ans

# the above solution is essentially the same as the following:
class Solution:
    def maximumXOR(self, A: List[int]) -> int:
        ans = 0
        for x in A: ans |= x
        return ans
        
        
"""
3:011
2:010
4:100
6:110

3:011
2:010
4:100
2:010
"""
"""
110 & 010 = 010
"""

"""
00001
00010
00011
01001
00010

01011
"""