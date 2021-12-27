""" L0: https://aaronice.gitbook.io/lintcode/sweep-line/meeting-rooms
"""
class Solution:
    def canAttendMeetings(self, A):
        A = sorted(A, key=lambda x: x[1])
        start = A[0][1]
        for s, e in A[1:]:
            if s<start: return False
            else: start = s
        return True

interval = [[7,10],[2,4]]
sol = Solution()
ans = sol.canAttendMeetings(interval)
print(ans)
