""" https://leetcode.com/problems/minimum-operations-to-make-the-array-alternating/
At the end we only have two distinct numbers in the array,
so the key is to translate the problem into greedily find the most frequent elements in odd and even positions.

1. use two counters to record odd and even position's value and then sort them
2. greedily find maximal frequency by:
    if the most frequent element are not the same, then return the remaining elements
    else select first odd and second even frequent elemnts or select first even and second old frequent element
"""


class Solution:
    def minimumOperations(self, A: List[int]) -> int:
        if len(A) == 1:
            return 0

        odd, even = A[::2], A[1::2]
        odd = sorted(Counter(odd).items(), key=lambda x: -x[1])
        even = sorted(Counter(even).items(), key=lambda x: -x[1])

        if odd[0][0] != even[0][0]:
            return len(A) - odd[0][1] - even[0][1]
        else:
            # select first odd and second even frequencies
            a = len(A) - odd[0][0] - (even[1][0] if len(even) > 1 else 0)
            # select first even and second old frequencies
            b = len(A) - even[0][0] - (odd[1][0] if len(odd) > 1 else 0)
            return min(a, b)
