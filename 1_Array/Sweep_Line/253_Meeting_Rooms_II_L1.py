class Solution:
    def minMeetingRooms(self, intervals):
        n = max([i.end for i in intervals])
        cnt = [0]*(n+1)
        for i in intervals:
            cnt[i.start] += 1
            cnt[i.end] -= 1
        for i in range(1, n+1):
            cnt[i] += cnt[i-1]
        return max(cnt)