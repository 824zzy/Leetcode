""" https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/
Iterate from A to Z instead of the array elements.
For each character, count how many times it appears in the unique character strings.

1. From A to Z, find all the indexes of every characters
2. Given ...XXXA[XXAXX]AXX.., the answer of j should be (A[j]-A[i])*(A[k]-A[j])
               i   j   k
"""
class Solution:
    def uniqueLetterString(self, s: str) -> int:
        locs = [[-1] for _ in range(26)]
        for i, x in enumerate(s): locs[ord(x)-65].append(i)
        locs = [x+[len(s)] for x in locs]
            
        ans = 0 
        for i in range(26): 
            for k in range(1, len(locs[i])-1): 
                ans += (locs[i][k] - locs[i][k-1]) * (locs[i][k+1] - locs[i][k])
        return ans  