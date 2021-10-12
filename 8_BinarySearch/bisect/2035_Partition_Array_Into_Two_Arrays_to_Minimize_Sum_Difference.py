""" L3: https://leetcode.com/problems/partition-array-into-two-arrays-to-minimize-sum-difference/
goal: 
    2*(Lcomb+Rcomb)+diff=sumA ==> 
    diff = sumA-2*(Lcomb+Rcomb) = L+R-2*Lcomb-2*Rcomb = (L-2*Lcomb)+(R-2*Rcomb)
    find minimum diff.
    
Let l = (L-2*Lcomb), r = (R-2*Rcomb)
given -r(for minimum diff), use bisect to find closest l.
"""
class Solution:
    def minimumDifference(self, A: List[int]) -> int:        
        # reduce time complexity from 2**30 to 2**15
        n = len(A)//2
        L, R = A[:n], A[n:]
        Lsum, Rsum = sum(L), sum(R)

        ans = float('inf')
        for i in range(1, n+1):
            # find all target candidate by combination
            Lcands = sorted(2*sum(combo)-Lsum for combo in combinations(L, i))
            for Rcand in combinations(R, n-i):
                r = 2*sum(Rcand)-Rsum
                idx = bisect_left(Lcands, -r)
                if idx: ans = min(ans, abs(Lcands[idx-1]+r))
                if idx<len(Lcands): ans = min(ans, abs(Lcands[idx]+r))
        return ans
