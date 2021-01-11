class Solution:
    def nextGreatestLetter(self, A: List[str], t: str) -> str:
        if ord(t)>=ord(A[-1]): return A[0]
        l, r = 0, len(A)-1
        while l<=r:
            m = (l+r)//2
            if ord(A[m])>ord(t): r = m - 1
            else: l = m + 1
        return A[l]