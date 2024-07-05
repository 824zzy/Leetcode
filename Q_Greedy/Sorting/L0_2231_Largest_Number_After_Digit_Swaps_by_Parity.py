""" https://leetcode.com/problems/largest-number-after-digit-swaps-by-parity/
1. find indexes of odd and even elements
2. sort odd and even elements
3. greedily reconstruct the largest number
"""


class Solution:
    def largestInteger(self, num: int) -> int:
        idx = [1 if int(x) & 1 else 0 for x in str(num)]
        odd = [c for i, c in enumerate(str(num)) if int(c) & 1]
        even = [c for i, c in enumerate(str(num)) if not int(c) & 1]
        odd.sort(reverse=True)
        even.sort(reverse=True)

        ans = []
        for i in idx:
            if i:
                ans.append(odd.pop(0))
            else:
                ans.append(even.pop(0))
        return int(str("".join(ans)))
