""" https://leetcode.com/problems/reduce-array-size-to-the-half/
Use sorted Counter to find minimal size to reach len(A)//2
"""


class Solution:
    def minSetSize(self, A: List[int]) -> int:
        cnt = Counter(A)
        ans = 0
        for i, v in enumerate(sorted(cnt.values(), reverse=True)):
            ans += v
            if ans >= len(A) // 2:
                return i + 1
