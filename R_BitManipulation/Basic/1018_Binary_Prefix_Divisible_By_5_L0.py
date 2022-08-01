""" https://leetcode.com/problems/binary-prefix-divisible-by-5/
update i on the fly and check if i is divisible by 5
""" 
class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        i = 0
        ans = []
        for x in A:
            i <<= 1
            i += x
            ans.append(i%5==0)
        return ans