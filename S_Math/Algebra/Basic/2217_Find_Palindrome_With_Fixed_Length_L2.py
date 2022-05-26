""" https://leetcode.com/problems/find-palindrome-with-fixed-length/
1. only the first half of palindrome matters to the order
2. make query palinedrome by add its reversed string
"""
class Solution:
    def kthPalindrome(self, A, l):
        base = 10 ** ((l - 1) // 2)
        ans = [int(q-1+base) for q in A]
        
        for i, x in enumerate(ans):
            if not l%2: x = str(x) + str(x)[::-1]
            else: x = str(x) + str(x)[:-1][::-1]
            if len(x) == l: ans[i] = int(x)
            else: ans[i] = -1
        return ans