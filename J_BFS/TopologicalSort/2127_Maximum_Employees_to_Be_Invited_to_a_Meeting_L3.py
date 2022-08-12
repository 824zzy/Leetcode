""" https://leetcode.com/problems/maximum-employees-to-be-invited-to-a-meeting/
learn from guan
there are only two cases can be considered as answer:
1. maximum circle that size is larger than 2
2. if circle size is 2, the answer is all the summation of links
"""
class Solution:
    def maximumInvitations(self, A: List[int]) -> int:
        inD = [0]*len(A)
        for i, j in enumerate(A):
            inD[j] += 1
        
        seen = [0]*len(A)
        depth = [1]*len(A)
        Q = []
        for i, d in enumerate(inD):
            if d==0:
                seen[i] = 1
                Q.append(i)
        
        while Q:
            i = Q.pop(0)
            j = A[i]
            inD[j] -= 1
            if not inD[j]:
                Q.append(j)
                seen[j] = 1
            depth[j] = depth[i]+1
        
        mx_circle = 0
        mx_link = 0
        for i in range(len(A)):
            if seen[i]==1: continue
            j = i
            cnt = 0
            while seen[j]==0:
                cnt += 1
                seen[j] = 1
                j = A[j]
            if cnt>2:
                mx_circle = max(mx_circle, cnt)
            elif cnt==2:
                mx_link += depth[i]+depth[A[i]]
        return max(mx_circle, mx_link)
