""" https://leetcode.com/problems/3sum-with-multiplicity/
"""


class Solution:
    def threeSumMulti(self, A: List[int], target: int) -> int:
        seen = defaultdict(int)
        ans = 0
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                rm = target - A[i] - A[j]
                if rm in seen:
                    ans += seen[rm]
            seen[A[i]] += 1
        return ans % (10 ** 9 + 7)
