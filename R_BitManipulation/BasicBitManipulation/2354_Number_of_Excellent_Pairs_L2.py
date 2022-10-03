""" https://leetcode.com/problems/number-of-excellent-pairs/
learn from lee215: https://leetcode.com/problems/number-of-excellent-pairs/discuss/2324984/JavaC%2B%2BPython-Inclusion-Exclusion-Principle

The Inclusion-Exclusion Principle
bits(num1 OR num2) + bits(num1 AND num2) = bits(num1) + bits(num2)

Time complexity: O(n*logn), where logn for bit count
"""
class Solution:
    def countExcellentPairs(self, A: List[int], k: int) -> int:
        c = Counter([x.bit_count() for x in set(A)])
        # O(32*32)
        return sum(c[k1]*c[k2] for k1 in c for k2 in c if k1 + k2 >= k)