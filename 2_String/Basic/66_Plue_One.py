""" ''.join(list) for calculation
"""
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int(''.join([str(s) for s in digits]))
        num += 1
        return [int(i) for i in str(num)]
        