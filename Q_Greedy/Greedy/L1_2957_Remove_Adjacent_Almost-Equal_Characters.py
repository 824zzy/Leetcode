""" https://leetcode.com/problems/remove-adjacent-almost-equal-characters/
greedily change the right character
"""


class Solution:
    def removeAlmostEqualCharacters(self, A: str) -> int:
        A = list(A)
        ans = 0
        for i in range(1, len(A)):
            if abs(ord(A[i]) - ord(A[i - 1])) <= 1:
                A[i] = "*"
                ans += 1
        return ans


"""
"aaaaa"
"abddez"
"zyxyxyz"
"""
