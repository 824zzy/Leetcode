""" Typical Hash Table
"""
# Concise solution
from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)

        odd, even = [v for v in counter.values() if v%2==1], [v for v in counter.values() if v%2==1]

        ans = sum(even) if len(even)!=0 else 0
        ans += sum(odd)-len(odd)+1 if len(odd)!=0 else 0

        return ans

# My silly solution long times ago
class Solution:
    def longestPalindrome(self, s: str) -> int:
        words = dict()
        count = 0
        flag = True
        
        for e in s:
            if e in words.keys():
                words[e] += 1
            else:
                words[e] = 1

        for k, v in words.items():
            if v % 2:
                count = count + v - 1
                if flag:
                    count += 1
                    flag = False
            else:
                count = count + v
        return count