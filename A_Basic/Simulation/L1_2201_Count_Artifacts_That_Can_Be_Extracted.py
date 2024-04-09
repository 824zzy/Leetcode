""" https://leetcode.com/problems/count-artifacts-that-can-be-extracted/
Since artifacts[i].length == 4 and 1 <= n <= 1000, brute force enumerate is acceptable.
"""


class Solution:
    def digArtifacts(self,
                     n: int,
                     A: List[List[int]],
                     dig: List[List[int]]) -> int:
        dig = set((d0, d1) for d0, d1 in dig)
        ans = 0

        for i, (r1, c1, r2, c2) in enumerate(A):
            extracted = True
            for r in range(r1, r2 + 1):
                if extracted:
                    for c in range(c1, c2 + 1):
                        if (r, c) not in dig:
                            extracted = False
                else:
                    break
            if extracted:
                ans += 1
        return ans

# elegent solution from ye15: optimize `extracted` flag by for-else statement


class Solution:
    def digArtifacts(self,
                     n: int,
                     A: List[List[int]],
                     dig: List[List[int]]) -> int:
        dig = set((d0, d1) for d0, d1 in dig)
        ans = 0

        for i, (r1, c1, r2, c2) in enumerate(A):
            for r in range(r1, r2 + 1):
                for c in range(c1, c2 + 1):
                    if (r, c) not in dig:
                        break
                else:
                    continue  # if all (r, c) in dig
                break  # if any (r, c) not in dig, then ans won't exist
            else:
                ans += 1
        return ans
