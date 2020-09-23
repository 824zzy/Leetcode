class Solution:
    def findLucky(self, arr: List[int]) -> int:
        cand = [k for k, v in collections.Counter(arr).items() if k==v]
        return max(cand) if cand else -1