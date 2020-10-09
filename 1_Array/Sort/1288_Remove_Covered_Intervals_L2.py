class Solution:
    def removeCoveredIntervals(self, A: List[List[int]]) -> int:
        A = sorted(A, key=lambda x:(x[0], -x[1]))
        ans = 0
        right = 0

        for i in range(len(A)):
            if A[i][1]>right:
                ans += 1
            right = max(right, A[i][1])
        return ans
    

# dumb solution
class Solution:
    def removeCoveredIntervals(self, A: List[List[int]]) -> int:
        ans = len(A)
        seen = set()
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                l, r = A[i], A[j]
                if l[0]<=r[0] and l[1]>=r[1]:
                    if tuple(r) not in seen:
                        ans -= 1
                    seen.add(tuple(r))    
                elif l[0]>=r[0] and l[1]<=r[1]:
                    if tuple(l) not in seen:
                        ans -= 1
                    seen.add(tuple(l))
        return ans