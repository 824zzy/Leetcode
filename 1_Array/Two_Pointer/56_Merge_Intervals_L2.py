class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        curr = 0
        for i in range(1, len(intervals)):
            if intervals[curr][1]>=intervals[i][0]:
                intervals[curr][1] = max(intervals[curr][1], intervals[i][1])
            else:
                curr += 1
                intervals[curr] = intervals[i]
        return intervals[:curr+1]