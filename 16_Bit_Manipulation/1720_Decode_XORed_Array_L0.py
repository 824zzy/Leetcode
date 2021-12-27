class Solution:
    def decode(self, A: List[int], f: int) -> List[int]:
        ans = [f]
        for a in A:
            f ^= a
            ans.append(f)
        return ans