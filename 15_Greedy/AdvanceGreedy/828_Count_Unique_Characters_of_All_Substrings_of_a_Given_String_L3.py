""" https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/
idea from lee: https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/discuss/128952/C%2B%2BJavaPython-One-pass-O(N)
code from ye: https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/discuss/1377763/Python3-greedy
"""
class Solution:
    def uniqueLetterString(self, s: str) -> int:
        locs = [[-1] for _ in range(26)]
        for i, x in enumerate(s): locs[ord(x)-65].append(i)
        locs = [locs[i]+[len(s)] for i in range(26)]
        
        ans = 0 
        for i in range(26):
            for j in range(1, len(locs[i])-1): 
                ans += (locs[i][j] - locs[i][j-1]) * (locs[i][j+1] - locs[i][j])
        return ans 