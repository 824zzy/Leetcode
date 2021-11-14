class Solution:
    def bitwiseComplement(self, N: int) -> int:
        return int(''.join(['0' if c=='1' else '1' for c in bin(N)[2:]]), 2)