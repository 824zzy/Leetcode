class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        mapping = {i: c for i, c in zip(indices, s)}
        return ''.join([i[1] for i in sorted(mapping.items())])
