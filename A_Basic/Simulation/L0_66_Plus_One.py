# Google
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = [str(d) for d in digits]
        digits = str(int(''.join(digits)) + 1)
        return [d for d in digits]
