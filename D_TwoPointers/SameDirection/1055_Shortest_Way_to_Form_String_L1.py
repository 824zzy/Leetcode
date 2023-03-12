""" https://leetcode.com/problems/shortest-way-to-form-string/
greedily find the longest substring of T that can be formed by concatenating some number of S's

Time complexity: O(m*n)
"""
class Solution:
    def shortestWay(self, S: str, T: str) -> int:
        j = 0
        ans = 0
        while 1:
            f = False
            for i in range(len(S)):
                if S[i]==T[j]:
                    j += 1
                    f = True
                if j==len(T): return ans+1
            if not f: return -1
            ans += 1
        return ans
    
"""
"abc"
"abcbc"
"abc"
"acdbc"
"xyz"
"xzyxz"
"aaaaa"
"aaaaaaaaaaaaa"
"""