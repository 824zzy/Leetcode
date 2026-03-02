""" https://leetcode.com/problems/maximum-strong-pair-xor-i/
Brute force all pairs. A pair (x, y) is "strong" if |x-y| <= min(x, y).
Check every pair and track the max XOR. O(n^2) is fine since n <= 50.
The hard version (LC 2935) requires a Trie + sliding window approach.
"""


class Solution:
    def maximumStrongPairXor(self, A: List[int]) -> int:
        ans = 0
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                if abs(A[i] - A[j]) <= min(A[i], A[j]):
                    ans = max(ans, A[i] ^ A[j])
        return ans
