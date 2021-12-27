class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        ans = 0
        last = -1
        for curr in range(len(seats)):
            if seats[curr]:
                if last<0:
                    ans = max(ans, curr)
                else:
                    ans = max(ans, (curr-last)//2)
                last = curr
        return max(ans, len(seats)-last-1)