""" https://leetcode.com/problems/meeting-rooms/
greedily or use sweep line template
"""
class Solution:
    def minMeetingRooms(self, intervals):
        n = max([j for i, j in intervals])
        cnt = [0]*(n+1)
        for i, j in intervals:
            cnt[i] += 1
            cnt[j] -= 1
        for i in range(1, n+1):
            cnt[i] += cnt[i-1]
        return max(cnt)
    
T = [
    [[0, 30], [5, 10], [15, 20]],
    [[7, 10], [2, 4]]
]
sol = Solution()
for t in T:
    ans = sol.minMeetingRooms(t)
    print(ans)