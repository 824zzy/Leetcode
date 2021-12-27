class Solution:
    def findMinArrowShots(self, A: List[List[int]]) -> int:
        A = sorted(A, key=lambda x: x[1])
        ans = [A[0]]
        for i in range(1, len(A)):
            if A[i][0]>ans[-1][1]: ans.append(A[i])
        return len(ans)