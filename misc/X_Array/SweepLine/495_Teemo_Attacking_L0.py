class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries: return 0
        n = timeSeries[-1]+duration
        count = [0] * (n+2)
        for i in timeSeries:
            count[i] += 1
            count[i+duration] -= 1
        for i in range(1, n+1):
            count[i] += count[i-1]
        return sum([1 for c in count if c!=0])