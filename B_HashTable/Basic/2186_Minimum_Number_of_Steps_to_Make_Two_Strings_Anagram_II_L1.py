""" https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram-ii/
find difference set by hash table operation or for loop
"""
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        fs, ft = Counter(s), Counter(t)
        return sum((fs-ft).values()) + sum((ft-fs).values())
    
    
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        cnts, cntt = Counter(s), Counter(t)
        ans = 0
        for k, v in cnts.items():
            d = v-cntt[k]
            if d>0: ans += d
        
        for k, v in cntt.items():
            d = v-cnts[k]
            if d>0: ans += d
        return ans