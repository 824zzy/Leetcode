""" https://leetcode.com/problems/find-the-longest-semi-repetitive-substring/
adjust window when cnt>1
"""
# two pointers/sliding window
class Solution:
    def longestSemiRepetitiveSubstring(self, A: str) -> int:
        n = len(A)
        ans = 1
        i = 0
        cnt = 0
        for j in range(1, n):
            if A[j]==A[j-1]:
                cnt += 1
            while cnt>1:
                i += 1
                if A[i]==A[i-1]:
                    cnt -= 1
            ans = max(ans, j-i+1)
        return ans

# brute force since 1 <= s.length <= 50
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            cnt = 0
            for j in range(i, len(s)):
                if j-i>0 and s[j]==s[j-1]:
                    cnt += 1
                    if cnt>1:
                        ans = max(ans, j-i)
                        break
            else:
                ans = max(ans, j-i+1)
        return ans
    
"""
"52233"
"5494"
"1111111"
"0010"
"0001"
"""