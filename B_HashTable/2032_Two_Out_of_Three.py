""" L0: https://leetcode.com/problems/two-out-of-three/
"""


class Solution:
    def twoOutOfThree(self, A: List[int], B: List[int], C: List[int]) -> List[int]:
        A, B, C = list(set(A)), list(set(B)), list(set(C))
        cnt = Counter(A + B + C)
        return [k for k, v in cnt.items() if v > 1]
