""" https://leetcode.com/problems/repeated-substring-pattern/submissions/
greedily check substring that can form the original string
""" 
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(1, len(s)//2+1):
            sub = s[:i]
            if sub*(len(s)//i) == s: return True
        return False