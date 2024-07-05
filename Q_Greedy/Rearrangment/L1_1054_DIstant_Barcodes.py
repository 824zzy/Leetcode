""" https://leetcode.com/problems/reorganize-string/
767 and 1054 are the same

Translate the problem to: rearrange characters to ensure no two adjacent projects are the same.
So based on characters frequency, we can fill the string by odd position first, then even positions.
"""


class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        cnt = Counter(barcodes)
        A = sorted([[v, k] for k, v in cnt.items()], reverse=True)
        ans = [""] * len(barcodes)
        i = 0

        if A[0][0] > (len(barcodes) + 1) / 2:
            return ""
        for v, k in A:
            for _ in range(v):
                ans[i] = k
                i += 2
                if i >= len(barcodes):
                    i = 1
        return "".join(anbarcodes)
