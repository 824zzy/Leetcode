""" https://leetcode.com/problems/maximum-split-of-positive-even-integers/
We cannot split odd numbers, and we can always split even ones.

Since split numbers must be unique, the best strategy is to use the smallest possible numbers (2, 4, 6, ... and so on) first.

At some point, we won't be able to split the remaining sum without repeating a previously used number (sum - cur < cur + 2). So, that remaining sum will be our last number in the split sequence.
"""


class Solution:
    def maximumEvenSplit(self, n: int) -> List[int]:
        if n & 1 == 1:
            return []
        x = 2
        ans = []
        while n >= x:
            ans.append(x)
            n -= x
            x += 2
        ans[-1] += n
        return ans
