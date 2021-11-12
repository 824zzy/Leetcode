class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        s = []
        t = float('inf')
        for n in nums:
            while s and n<=s[-1]:
                s.pop()
            if n>t: return True
            if s: t = min(t, n)
            s.append(n)
        return False