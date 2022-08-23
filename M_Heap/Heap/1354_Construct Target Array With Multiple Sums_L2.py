""" https://leetcode.com/problems/construct-target-array-with-multiple-sums/
optimized solution by modulus.
""" 
class Solution:
    def isPossible(self, A: List[int]) -> bool:
        A = [-x for x in A]
        heapify(A)
        sm = -1*sum(A)
        while A[0]<-1: 
            mx = -1*heappop(A)
            others = sm-mx
            if others==0 or mx<=others: return False 
            nxt = mx%others
            if nxt==0: nxt = others
                
            sm = others+nxt
            heappush(A, -nxt)
        return True