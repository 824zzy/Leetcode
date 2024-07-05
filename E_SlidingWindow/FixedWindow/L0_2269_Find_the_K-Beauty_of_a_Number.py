""" https://leetcode.com/problems/find-the-k-beauty-of-a-number/
linear scan by size fixed sliding window

or simply bruteforce
"""


class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        A = str(num)
        seen = []
        ans = 0
        for i in range(len(A)):
            seen += A[i]
            if i >= k:
                seen.pop(0)
            if len(seen) == k and int("".join(seen)) and num % int("".join(seen)) == 0:
                ans += 1
        return ans


class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        A = str(num)
        ans = 0
        for i in range(len(A) - k + 1):
            if int(A[i : i + k]) and not num % int(A[i : i + k]):
                ans += 1
        return ans
