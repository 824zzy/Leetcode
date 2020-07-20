class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        num2rank = {}
        sorted_arr = sorted(arr)
        rank = 1
        for n in sorted_arr:
            if n not in num2rank:
                num2rank[n] = rank
                rank += 1
        return [num2rank[a] for a in arr]