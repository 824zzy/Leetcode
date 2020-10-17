from collections import defaultdict
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        reachable = defaultdict(set)
        S = set(stones)
        if stones[0]+1 not in S:
            return False
        reachable[stones[0]+1] = {stones[0]}
        for curr in stones[1:]:
            for pre in reachable[curr]:
                dis = curr - pre
                if dis+curr in S:
                    reachable[dis+curr].add(curr)
                if dis+curr+1 in S:
                    reachable[dis+curr+1].add(curr)
                if dis>1 and dis+curr-1 in S:
                    reachable[dis+curr-1].add(curr)
        return len(reachable[stones[-1]])>0
    

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return 0
        
        def search(l, i, j):
            while i<=j:
                m = (i+j)//2
                if l[m]==target:
                    return True
                if l[m]<target:
                    i = m+1
                elif l[m]>target:
                    j = m-1
            return False
        
        new_m = [n for m in matrix for n in m]
        ans = search(new_m, 0, len(new_m)-1)
        return ans