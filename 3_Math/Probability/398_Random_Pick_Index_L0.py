class Solution:
    def __init__(self, nums: List[int]):
        self.d = collections.defaultdict(list)
        for i, n in enumerate(nums):
            self.d[n].append(i)

    def pick(self, target: int) -> int:
        cnt, ans = 0, 0
        for i in range(len(self.d[target])):
            cnt += 1
            p = random.random()
            if p < 1/cnt:
                ans = self.d[target][i]
        return ans