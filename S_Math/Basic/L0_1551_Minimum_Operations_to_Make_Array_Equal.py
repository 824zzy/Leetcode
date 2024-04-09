""" https://leetcode.com/problems/minimum-operations-to-make-array-equal/
simulate the process, all the elements will convert to n itself

Or use arithmetic progression formula:
Observation:
if n is odd, say 3, the answer is 2
[1,3,5]
2+0+2

if n is even, say 6, the answer is 1+3+5
[1,3,5,7,9,11]
5+3+1+1+3+5

Conclusion: there are n//2 items, and answer is n*a1+(n-1)*d/2, where a1=2 if n is odd else a1=1
"""


class Solution:
    def minOperations(self, n: int) -> int:
        ans = 0
        for i in range(n):
            ans += abs(2 * i + 1 - n)
        return ans // 2


class Solution:
    def minOperations(self, n: int) -> int:
        if n & 1:
            n //= 2
            return 2 * n + n * (n - 1) * 2 // 2
        else:
            n //= 2
            return n + n * (n - 1) * 2 // 2
