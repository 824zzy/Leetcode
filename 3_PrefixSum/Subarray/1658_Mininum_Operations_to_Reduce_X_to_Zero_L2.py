""" https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/
https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/discuss/935986/Python3-O(N)-hash-table-of-prefix
Translate the problem into: find a subarray which sum is sum(A)-x and has maximal length.
"""
class Solution:
    def minOperations(self, A: List[int], x: int) -> int:
        x = sum(A)-x
        if not x: return len(A)
        seen = {0: -1}
        prefix = 0
        ans = 0
        
        for i, n in enumerate(A):
            prefix += n
            if prefix-x in seen: ans = max(ans, i-seen[prefix-x])
            seen.setdefault(prefix, i)
        return len(A)-ans if ans else -1