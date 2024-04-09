""" https://leetcode.com/problems/longest-repeating-substring/
binary search to find the length of the longest repeating substring

Note: don't use tuple to store the substring.
"""
# binary search


class Solution:
    def longestRepeatingSubstring(self, A: str) -> int:
        A += '*'

        def fn(x):
            seen = set()
            w = A[:x]
            seen.add(w)
            for i in range(x, len(A)):
                w = w[1:] + A[i]
                if w in seen:
                    return False
                seen.add(w)
            return True

        l, r = 1, len(A)
        while l < r:
            m = (l + r) // 2
            x = fn(m)
            if x:
                r = m
            else:
                l = m + 1
        return l - 1


# brute force
class Solution:
    def longestRepeatingSubstring(self, A: str) -> int:
        seen = set()
        ans = 0
        for i in range(len(A)):
            t = ''
            for j in range(i, len(A)):
                t += A[j]
                if t in seen:
                    ans = max(ans, len(t))
                seen.add(t)
        return ans


"""
"abcd"
"abbaba"
"aabcaabdaab"
"aaaaa"
"""
