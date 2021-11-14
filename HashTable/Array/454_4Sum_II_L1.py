class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        AB, CD = collections.Counter(), collections.Counter()
        for a in A:
            for b in B:
                AB[-(a+b)] += 1
        for c in C:
            for d in D:
                CD[c+d] += 1
        return sum([CD[ab]*AB[ab] for ab in AB])