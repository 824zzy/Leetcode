""" https://leetcode.com/problems/find-substring-with-given-hash-value/
https://leetcode.com/problems/find-substring-with-given-hash-value/discuss/1730321/JavaC%2B%2BPython-Sliding-Window-%2B-Rolling-Hash
Calculate the rolling hash backward.
In this process, we slide a window of size k from the end to the begin.

Firstly calculate the substring hash of the last k characters,
then we add one previous backward and drop the last characters.
"""


class Solution:
    def subStrHash(self, s: str, p: int, m: int, k: int, hashValue: int) -> str:
        def val(c):
            return ord(c) - ord("a") + 1

        ans = n = len(s)
        pk = pow(p, k, m)
        cur = 0

        for i in range(n - 1, -1, -1):
            cur = (cur * p + val(s[i])) % m
            if i + k < n:
                cur = (cur - val(s[i + k]) * pk) % m
            if cur == hashValue:
                ans = i
        return s[ans : ans + k]
