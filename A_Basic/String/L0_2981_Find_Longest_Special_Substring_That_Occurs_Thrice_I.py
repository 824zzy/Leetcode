""" https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-i/
since n<50, just brute force
"""
class Solution:
    def maximumLength(self, s: str) -> int:
        for l in reversed(range(1, len(s)+1)):
            for c in range(26):
                cnt = 0
                t = chr(c+97)*l
                for i in range(l, len(s)+1):
                    ss = s[i-l:i]
                    if ss==t:
                        cnt += 1
                        if cnt==3:
                            return l
        return -1
    
"""
"aaaa"
"abcdef"
"abcaba"
"cccerrrecdcdccedecdcccddeeeddcdcddedccdceeedccecde"
"""