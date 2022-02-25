""" https://leetcode.com/problems/count-number-of-teams/
"""
# top down
class Solution:
    def numTeams(self, A: List[int]) -> int:
        @cache
        def dp(i, k, mode):
            if i==len(A): return 0
            if k==0: return 1
            
            ans = 0
            for j in range(i, len(A)):
                if mode=='up' and A[i]<A[j]:
                    ans += dp(j, k-1, 'up')
                elif mode=='down' and A[i]>A[j]:
                    ans += dp(j, k-1, 'down')
            return ans
        
        return sum([dp(i, 2, 'up') for i in range(len(A))])+sum([dp(i, 2, 'down') for i in range(len(A))])

        
# O(N^2)
class Solution:
    def numTeams(self, A: List[int]) -> int:
        up = [0] * len(A)
        down = [0] * len(A)
        ans = 0
        for i in range(len(A)-1):
            for j in range(i+1, len(A)):
                if A[i] < A[j]: up[i] += 1
                else: down[i] += 1
                    
        for i in range(len(A)-1):
            for j in range(i+1, len(A)):
                if A[i] < A[j]: ans += up[j]
                else: ans += down[j]
        return ans


# O(N^3)
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        ans = 0
        for i in range(len(rating)):
            for j in range(i+1, len(rating)):
                for k in range(j+1, len(rating)):
                    if rating[i]<rating[j]<rating[k] or rating[i]>rating[j]>rating[k]:
                        ans += 1
        return ans