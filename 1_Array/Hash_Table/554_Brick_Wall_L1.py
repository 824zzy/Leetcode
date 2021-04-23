# Count gaps
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        cnt = Counter()
        for w in wall:
            r = 0
            for c in w[:-1]:
                r += c
                cnt[r] += 1
        if cnt: return len(wall)-cnt.most_common(1)[0][1]
        else: return len(wall)