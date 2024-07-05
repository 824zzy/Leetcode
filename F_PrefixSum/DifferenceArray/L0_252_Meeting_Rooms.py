""" https://leetcode.com/problems/meeting-rooms/
greedily or use sweep line template
"""


class Solution:
    def minMeetingRooms(self, A):
        A = sorted(A)
        for i in range(len(A)):
            if A[i][1] > A[i + 1][0]:
                return False
        return True


class Solution:
    def minMeetingRooms(self, A):
        _A = []
        for i, j in A:
            _A.append([i, 1])
            _A.append([j, -1])

        A = sorted(_A)
        cnt = 0
        for _, i in A:
            cnt += i
            if cnt > 1:
                return False
        return True


T = [[[0, 30], [5, 10], [15, 20]], [[7, 10], [2, 4]]]
sol = Solution()
for t in T:
    ans = sol.minMeetingRooms(t)
    print(ans)
