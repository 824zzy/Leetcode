""" Best solution with expand pointers
Especially for the palindrome questions
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2 or s==s[::-1]:
            return s
        
        l, r = 0, 0
        for i in range(len(s)):
            # check odd and even
            l, r = max((l, r), self.expand(s, i, i), self.expand(s, i, i+1),
                       key=lambda x: x[1]-x[0])
        return s[l:r]
    
    def expand(self, s: str, l: int, r:int) -> int:
        while l>=0 and r<len(s) and s[l]==s[r]:
            l, r = l-1, r+1
        return l+1, r
        

""" Sliding windows with advanced palindrome-judgement
3680ms, faster than vanilla palindrome-judgement
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ""

        window = len(s)

        while 1:
            for i in range(len(s)+1-window):
                subs = s[i:window+i]
                if subs == subs[::-1]:
                    return subs

            window -= 1


""" Sliding windows with vanilla palindrome-judgement
8556ms, slow enough.
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ""
        window = len(s)

        while 1:
            for i in range(len(s)+1-window):
                subs = s[i:window+i]
                is_palin = True
                for i in range(len(subs)):
                    if subs[i] != subs[-1-i]:
                        is_palin = False
                        break
                if is_palin:
                    return subs   
            window -= 1


""" Note that brute force not work! O(n^3)
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ''
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i:j+1] == s[i:j+1][::-1]:
                    ans = max(ans, s[i:j+1], key=len)
        return ans