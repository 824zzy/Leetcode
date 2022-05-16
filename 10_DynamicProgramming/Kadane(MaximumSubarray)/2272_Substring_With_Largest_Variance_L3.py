""" https://leetcode.com/problems/substring-with-largest-variance/
For each character pair {a, b}, using two pass Kadane algorithm to find the largest variance.
Since the substring must has at least one "-1", dp1[i]+dp2[i]-A[i] must be applied to find left most and right most largest variance at index i.

idea is learned from guan: https://www.youtube.com/watch?v=tMIBXRhp9hs
"""
class Solution:
    def largestVariance(self, s: str) -> int:
        cnt = Counter(s)
        ans = 0
        
        def fn(A):
            # two pass Kadane
            dp1 = [0] * len(A)
            dp1[0] = A[0]
            for i in range(1, len(A)):
                dp1[i] = max(dp1[i-1]+A[i], A[i])
                
            dp2 = [0] * len(A)
            dp2[-1] = A[-1]
            ans = dp1[-1]+dp2[-1]-A[-1] if A[-1]==-1 else 0
            for i in reversed(range(len(A)-1)):
                dp2[i] = max(dp2[i+1]+A[i], A[i]) 
                if A[i]==-1: 
                    ans = max(ans, dp1[i]+dp2[i]-A[i])
            return ans
            
        for a in cnt:
            for b in cnt:
                if a==b: continue
                A = []
                for k in range(len(s)):
                    if a==s[k]: A.append(1)
                    elif b==s[k]: A.append(-1)
                    
                ans = max(ans, fn(A))
        return ans