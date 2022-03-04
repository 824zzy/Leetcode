class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        d = [[a, bin(a).count('1')] for a in arr]
        return [k for k, v in sorted(d, key=lambda x: (x[1], x[0]))]