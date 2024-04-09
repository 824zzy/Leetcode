""" https://leetcode.com/problems/count-beautiful-substrings-i/
brute force
"""


class Solution:
    def beautifulSubstrings(self, A: str, k: int) -> int:
        ans = 0
        for i in range(len(A)):
            v, c = 0, 0
            for j in range(i, len(A)):
                if A[j] in 'aeiou':
                    v += 1
                else:
                    c += 1
                if v == c and (v * c) % k == 0:
                    ans += 1
        return ans


"""
"baeyh"
2
"abba"
1
"bcdf"
1
"""
