class Solution:
    def findMinArrowShots(self, A: List[List[int]]) -> int:
        A = sorted(A, key=lambda x: (x[1]))
        ans = 0
        right = float('-inf')
        for i in range(len(A)):
            if A[i][0]>right:
                right = A[i][1]
                ans += 1
        return ans