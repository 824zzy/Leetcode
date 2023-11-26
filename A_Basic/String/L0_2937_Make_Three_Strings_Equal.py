""" https://leetcode.com/problems/make-three-strings-equal/
convert the problem into: compute the longest common prefix
"""
class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        same = 0
        for i, (x, y, z) in enumerate(zip(s1, s2, s3)):
            if x!=y or x!=z:
                if i==0: return -1
                break
            same += 3
        return len(s1)+len(s2)+len(s3)-same
    
    
"""
"abc"
"abb"
"ab"
"dac"
"bac"
"cac"
"""